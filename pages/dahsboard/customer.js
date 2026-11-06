/**
 * Customer Dashboard Component (Vanilla JavaScript)
 */
function renderCustomerDashboard(container) {
  const token = localStorage.getItem("jwt_token");
  const userType = localStorage.getItem("user_type");
  const userEmail = localStorage.getItem("user_email") || "Customer";

  // Route protection
  if (!token || userType !== "customer") {
    alert("Unauthorized access. Redirecting to sign in.");
    window.Router.navigate("/pages/auth/signIn.js");
    return;
  }

  container.innerHTML = `
    <div class="dashboard-container">
      <header class="dashboard-header">
        <div class="user-info">
          <h2>Customer Portal</h2>
          <span class="badge badge-customer">CUSTOMER ACCOUNT</span>
          <span class="user-email-label">Welcome, <strong>${userEmail}</strong></span>
        </div>
        <div class="header-actions">
          <div class="idle-timer-box" title="Any user interaction resets this timer">
            ⏱ Inactivity Timeout: <span id="idle-countdown-display" class="countdown-highlight">120s</span>
          </div>
          <button id="signout-btn" class="btn btn-secondary">Sign Out</button>
        </div>
      </header>

      <section class="session-notice">
        <p>🔒 <strong>Protected Session:</strong> For your security, this session will expire after <strong>120 seconds</strong> of inactivity. Typing or clicking will keep you signed in.</p>
      </section>

      <div id="customer-content-loading" class="loading-state">
        <div class="spinner"></div>
        <p>Retrieving your account information...</p>
      </div>

      <div id="customer-content" class="hidden">
        <div class="metrics-grid">
          <div class="metric-card">
            <h3>Account Number</h3>
            <p class="metric-value font-mono" id="cust-member-id">---</p>
          </div>
          <div class="metric-card">
            <h3>Membership Tier</h3>
            <p class="metric-value text-accent" id="cust-tier">---</p>
          </div>
          <div class="metric-card">
            <h3>Reward Points</h3>
            <p class="metric-value" id="cust-points">0</p>
          </div>
          <div class="metric-card">
            <h3>Member Since</h3>
            <p class="metric-status" id="cust-since">---</p>
          </div>
        </div>

        <div class="table-section">
          <div class="table-header">
            <h3>My Orders & Services</h3>
            <button id="refresh-customer-data" class="btn btn-small">↻ Refresh</button>
          </div>
          <div class="table-wrapper">
            <table class="data-table">
              <thead>
                <tr>
                  <th>Order Reference</th>
                  <th>Service Description</th>
                  <th>Status</th>
                  <th>Amount</th>
                </tr>
              </thead>
              <tbody id="orders-table-body">
                <!-- Orders populated via API -->
              </tbody>
            </table>
          </div>
        </div>
      </div>
    </div>
  `;

  // Bind Buttons
  document.getElementById("signout-btn").addEventListener("click", () => {
    window.Router.signOut("You have signed out successfully.");
  });

  document.getElementById("refresh-customer-data").addEventListener("click", () => {
    loadCustomerData();
  });

  // Fetch customer data from backend
  async function loadCustomerData() {
    try {
      const response = await fetch("/api/dashboard/customer", {
        headers: {
          "Authorization": `Bearer ${token}`
        }
      });

      const data = await response.json();

      if (!response.ok || !data.success) {
        if (response.status === 401) {
          window.Router.signOut("Session expired or invalid token. Please sign in again.");
          return;
        }
        throw new Error(data.error || "Failed to load customer profile");
      }

      // Populate Account Information
      document.getElementById("cust-member-id").textContent = data.dashboard.account.member_id;
      document.getElementById("cust-tier").textContent = data.dashboard.account.tier;
      document.getElementById("cust-points").textContent = data.dashboard.account.reward_points.toLocaleString();
      document.getElementById("cust-since").textContent = data.dashboard.account.member_since;

      // Populate Orders Table
      const tbody = document.getElementById("orders-table-body");
      tbody.innerHTML = "";

      data.dashboard.orders.forEach(ord => {
        const tr = document.createElement("tr");
        tr.innerHTML = `
          <td><code>${ord.id}</code></td>
          <td><strong>${ord.service}</strong></td>
          <td><span class="badge badge-${ord.status === 'Completed' ? 'success' : 'pending'}">${ord.status}</span></td>
          <td>${ord.amount}</td>
        `;
        tbody.appendChild(tr);
      });

      document.getElementById("customer-content-loading").classList.add("hidden");
      document.getElementById("customer-content").classList.remove("hidden");

    } catch (err) {
      alert("Error loading customer dashboard: " + err.message);
    }
  }

  loadCustomerData();
}

window.CustomerDashboardPage = { render: renderCustomerDashboard };


/**
 * Staff Dashboard Component (Vanilla JavaScript)
 */
function renderStaffDashboard(container) {
  const token = localStorage.getItem("jwt_token");
  const userType = localStorage.getItem("user_type");
  const userEmail = localStorage.getItem("user_email") || "Staff Member";

  // Route protection
  if (!token || userType !== "staff") {
    alert("Unauthorized access. Redirecting to sign in.");
    window.Router.navigate("/pages/auth/signIn.js");
    return;
  }

  container.innerHTML = `
    <div class="dashboard-container">
      <header class="dashboard-header">
        <div class="user-info">
          <h2>Staff Portal</h2>
          <span class="badge badge-staff">STAFF ACCESS</span>
          <span class="user-email-label">Logged in as: <strong>${userEmail}</strong></span>
        </div>
        <div class="header-actions">
          <button id="launch-ocr-btn" class="btn btn-primary btn-small">📄 Gemini Invoice OCR</button>
          <div class="idle-timer-box" title="Any user interaction resets this timer">
            ⏱ Inactivity Timeout: <span id="idle-countdown-display" class="countdown-highlight">120s</span>
          </div>
          <button id="signout-btn" class="btn btn-secondary">Sign Out</button>
        </div>
      </header>

      <section class="session-notice">
        <p>⚠️ <strong>Security Notice:</strong> Sessions automatically sign out after <strong>120 seconds</strong> of inactivity. User interaction (mouse, keyboard, click) resets the timer.</p>
      </section>

      <div id="staff-content-loading" class="loading-state">
        <div class="spinner"></div>
        <p>Loading real-time management data...</p>
      </div>

      <div id="staff-content" class="hidden">
        <div class="metrics-grid">
          <div class="metric-card">
            <h3>Total Registered</h3>
            <p class="metric-value" id="stat-total-users">0</p>
          </div>
          <div class="metric-card">
            <h3>Staff Members</h3>
            <p class="metric-value" id="stat-staff-count">0</p>
          </div>
          <div class="metric-card">
            <h3>Customers</h3>
            <p class="metric-value" id="stat-customer-count">0</p>
          </div>
          <div class="metric-card">
            <h3>System Status</h3>
            <p class="metric-status text-success" id="stat-system-status">Active</p>
          </div>
        </div>

        <div class="table-section">
          <div class="table-header">
            <h3>Registered User Directory</h3>
            <button id="refresh-staff-data" class="btn btn-small">↻ Refresh</button>
          </div>
          <div class="table-wrapper">
            <table class="data-table">
              <thead>
                <tr>
                  <th>ID</th>
                  <th>Email</th>
                  <th>Role</th>
                  <th>Created At</th>
                </tr>
              </thead>
              <tbody id="user-table-body">
                <!-- User rows populated via API -->
              </tbody>
            </table>
          </div>
        </div>
      </div>
    </div>
  `;

  // Bind Buttons
  document.getElementById("launch-ocr-btn").addEventListener("click", () => {
    window.Router.navigate("/pages/ocrService.js");
  });

  document.getElementById("signout-btn").addEventListener("click", () => {
    window.Router.signOut("You have signed out successfully.");
  });

  document.getElementById("refresh-staff-data").addEventListener("click", () => {
    loadStaffData();
  });

  // Fetch staff management data from backend
  async function loadStaffData() {
    try {
      const response = await fetch("/api/dashboard/staff", {
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
        throw new Error(data.error || "Failed to load staff data");
      }

      // Populate Metrics
      document.getElementById("stat-total-users").textContent = data.dashboard.stats.total_users;
      document.getElementById("stat-staff-count").textContent = data.dashboard.stats.staff_count;
      document.getElementById("stat-customer-count").textContent = data.dashboard.stats.customer_count;
      document.getElementById("stat-system-status").textContent = data.dashboard.stats.system_status;

      // Populate User Table
      const tbody = document.getElementById("user-table-body");
      tbody.innerHTML = "";

      data.dashboard.recent_users.forEach(u => {
        const tr = document.createElement("tr");
        tr.innerHTML = `
          <td>#${u.id}</td>
          <td><strong>${u.email}</strong></td>
          <td><span class="badge badge-${u.user_type}">${u.user_type.toUpperCase()}</span></td>
          <td>${u.created_at || 'Just now'}</td>
        `;
        tbody.appendChild(tr);
      });

      document.getElementById("staff-content-loading").classList.add("hidden");
      document.getElementById("staff-content").classList.remove("hidden");

    } catch (err) {
      alert("Error loading staff dashboard: " + err.message);
    }
  }

  loadStaffData();
}

window.StaffDashboardPage = { render: renderStaffDashboard };


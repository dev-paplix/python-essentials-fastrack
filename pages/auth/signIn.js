/**
 * Sign In Page Component (Vanilla JavaScript)
 */
function renderSignIn(container) {
  container.innerHTML = `
    <div class="auth-card">
      <div class="card-header">
        <div class="logo-icon">🔐</div>
        <h2>Sign In</h2>
        <p class="subtitle">Access your account and dashboard</p>
      </div>

      <div id="auth-alert" class="alert hidden"></div>

      <form id="signin-form" class="auth-form" onsubmit="event.preventDefault();">
        <div class="form-group">
          <label for="signin-email">Email Address</label>
          <input 
            type="email" 
            id="signin-email" 
            placeholder="e.g. staff@example.com" 
            required 
            autocomplete="email"
          />
        </div>

        <div class="form-group">
          <label for="signin-password">Password</label>
          <input 
            type="password" 
            id="signin-password" 
            placeholder="••••••••" 
            required 
            autocomplete="current-password"
          />
        </div>

        <button type="submit" id="signin-submit-btn" class="btn btn-primary">
          <span class="btn-text">Sign In</span>
          <span class="btn-spinner hidden"></span>
        </button>
      </form>

      <div class="card-footer">
        <p>Don't have an account? <a href="#/signup" id="go-to-signup">Sign Up</a></p>
        <div class="quick-credentials">
          <p class="text-muted"><strong>Default Demo Credentials:</strong></p>
          <p class="text-muted">Staff: <code>staff@example.com</code> / <code>staff123</code></p>
          <p class="text-muted">Customer: <code>customer@example.com</code> / <code>customer123</code></p>
        </div>
      </div>
    </div>
  `;

  // Bind Events
  const form = document.getElementById("signin-form");
  const emailInput = document.getElementById("signin-email");
  const passwordInput = document.getElementById("signin-password");
  const submitBtn = document.getElementById("signin-submit-btn");
  const alertBox = document.getElementById("auth-alert");

  document.getElementById("go-to-signup").addEventListener("click", (e) => {
    e.preventDefault();
    if (window.Router) {
      window.Router.navigate("/pages/auth/signUp.js");
    }
  });

  form.addEventListener("submit", async () => {
    const email = emailInput.value.trim();
    const password = passwordInput.value;

    if (!email || !password) {
      showAlert("Please enter both email and password.", "error");
      return;
    }

    setLoading(true);
    hideAlert();

    try {
      const response = await fetch("/api/auth/signin", {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify({ email, password })
      });

      const data = await response.json();

      if (!response.ok || !data.success) {
        throw new Error(data.error || "Authentication failed. Check your credentials.");
      }

      // Save token and user details in localStorage
      localStorage.setItem("jwt_token", data.token);
      localStorage.setItem("user_type", data.user.type);
      localStorage.setItem("user_email", data.user.email);
      localStorage.setItem("user_info", JSON.stringify(data.user));

      showAlert("Login successful! Redirecting to your dashboard...", "success");

      // Redirect user based on their type
      setTimeout(() => {
        if (data.user.type === "staff") {
          window.Router.navigate("/pages/dahsboard/staff.js");
        } else {
          window.Router.navigate("/pages/dahsboard/customer.js");
        }
      }, 700);

    } catch (err) {
      showAlert(err.message, "error");
    } finally {
      setLoading(false);
    }
  });

  function showAlert(message, type) {
    alertBox.textContent = message;
    alertBox.className = `alert alert-${type}`;
    alertBox.classList.remove("hidden");
  }

  function hideAlert() {
    alertBox.classList.add("hidden");
  }

  function setLoading(loading) {
    if (loading) {
      submitBtn.disabled = true;
      submitBtn.querySelector(".btn-text").textContent = "Signing In...";
      submitBtn.querySelector(".btn-spinner").classList.remove("hidden");
    } else {
      submitBtn.disabled = false;
      submitBtn.querySelector(".btn-text").textContent = "Sign In";
      submitBtn.querySelector(".btn-spinner").classList.add("hidden");
    }
  }
}

// Attach to window for vanilla JS modularity
window.SignInPage = { render: renderSignIn };


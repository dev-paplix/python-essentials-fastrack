/**
 * Sign Up Page Component (Vanilla JavaScript)
 */
function renderSignUp(container) {
  container.innerHTML = `
    <div class="auth-card">
      <div class="card-header">
        <div class="logo-icon">📝</div>
        <h2>Create Account</h2>
        <p class="subtitle">Join as Staff or Customer</p>
      </div>

      <div id="auth-alert" class="alert hidden"></div>

      <form id="signup-form" class="auth-form" onsubmit="event.preventDefault();">
        <div class="form-group">
          <label for="signup-email">Email Address</label>
          <input 
            type="email" 
            id="signup-email" 
            placeholder="e.g. user@example.com" 
            required 
            autocomplete="email"
          />
        </div>

        <div class="form-group">
          <label for="signup-password">Password (minimum 6 chars)</label>
          <input 
            type="password" 
            id="signup-password" 
            placeholder="••••••••" 
            minlength="6" 
            required 
            autocomplete="new-password"
          />
        </div>

        <div class="form-group">
          <label for="signup-type">Account Type</label>
          <select id="signup-type" required>
            <option value="customer" selected>Customer (Standard Client Portal)</option>
            <option value="staff">Staff (Administrative Portal)</option>
          </select>
          <small class="field-hint">Choose 'Staff' for administrative management or 'Customer' for client view.</small>
        </div>

        <button type="submit" id="signup-submit-btn" class="btn btn-primary">
          <span class="btn-text">Create Account</span>
          <span class="btn-spinner hidden"></span>
        </button>
      </form>

      <div class="card-footer">
        <p>Already have an account? <a href="#/signin" id="go-to-signin">Sign In</a></p>
      </div>
    </div>
  `;

  // Bind Events
  const form = document.getElementById("signup-form");
  const emailInput = document.getElementById("signup-email");
  const passwordInput = document.getElementById("signup-password");
  const typeSelect = document.getElementById("signup-type");
  const submitBtn = document.getElementById("signup-submit-btn");
  const alertBox = document.getElementById("auth-alert");

  document.getElementById("go-to-signin").addEventListener("click", (e) => {
    e.preventDefault();
    if (window.Router) {
      window.Router.navigate("/pages/auth/signIn.js");
    }
  });

  form.addEventListener("submit", async () => {
    const email = emailInput.value.trim();
    const password = passwordInput.value;
    const type = typeSelect.value;

    if (!email || !password || !type) {
      showAlert("Please fill in all required fields.", "error");
      return;
    }

    if (password.length < 6) {
      showAlert("Password must be at least 6 characters long.", "error");
      return;
    }

    setLoading(true);
    hideAlert();

    try {
      const response = await fetch("/api/auth/signup", {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify({ email, password, type })
      });

      const data = await response.json();

      if (!response.ok || !data.success) {
        throw new Error(data.error || "Failed to create account.");
      }

      // Store authenticated session
      localStorage.setItem("jwt_token", data.token);
      localStorage.setItem("user_type", data.user.type);
      localStorage.setItem("user_email", data.user.email);
      localStorage.setItem("user_info", JSON.stringify(data.user));

      showAlert(data.message || "Registration successful! Redirecting...", "success");

      // Redirect immediately to the corresponding dashboard
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
      submitBtn.querySelector(".btn-text").textContent = "Creating Account...";
      submitBtn.querySelector(".btn-spinner").classList.remove("hidden");
    } else {
      submitBtn.disabled = false;
      submitBtn.querySelector(".btn-text").textContent = "Create Account";
      submitBtn.querySelector(".btn-spinner").classList.add("hidden");
    }
  }
}

window.SignUpPage = { render: renderSignUp };


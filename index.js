/**
 * Application Entry & Router (Vanilla JavaScript)
 * Handles client-side navigation and the 120-second inactivity timeout.
 */

(function () {
  const TIMEOUT_SECONDS = 120;
  let idleSecondsRemaining = TIMEOUT_SECONDS;
  let idleIntervalId = null;
  let activityListenersBound = false;

  // -----------------------------------------------------------
  // 1. INACTIVITY TRACKER (120-Second Auto Sign-Out)
  // -----------------------------------------------------------
  function resetIdleTimer() {
    idleSecondsRemaining = TIMEOUT_SECONDS;
    updateTimerUI();
  }

  function updateTimerUI() {
    const display = document.getElementById("idle-countdown-display");
    if (display) {
      display.textContent = `${idleSecondsRemaining}s`;
      if (idleSecondsRemaining <= 20) {
        display.classList.add("countdown-warning");
      } else {
        display.classList.remove("countdown-warning");
      }
    }
  }

  function bindActivityEvents() {
    if (activityListenersBound) return;
    const events = ["mousemove", "mousedown", "keydown", "scroll", "touchstart", "click"];
    events.forEach((evt) => {
      window.addEventListener(evt, resetIdleTimer, { passive: true });
    });
    activityListenersBound = true;
  }

  function startIdleTracker() {
    stopIdleTracker();
    idleSecondsRemaining = TIMEOUT_SECONDS;
    bindActivityEvents();
    updateTimerUI();

    idleIntervalId = setInterval(() => {
      const token = localStorage.getItem("jwt_token");
      if (!token) {
        stopIdleTracker();
        return;
      }

      idleSecondsRemaining--;
      updateTimerUI();

      if (idleSecondsRemaining <= 0) {
        stopIdleTracker();
        handleInactivitySignOut();
      }
    }, 1000);
  }

  function stopIdleTracker() {
    if (idleIntervalId) {
      clearInterval(idleIntervalId);
      idleIntervalId = null;
    }
  }

  function handleInactivitySignOut() {
    localStorage.removeItem("jwt_token");
    localStorage.removeItem("user_type");
    localStorage.removeItem("user_email");
    localStorage.removeItem("user_info");

    alert("⚠️ Security Timeout: You have been signed out due to 120 seconds of inactivity.");
    window.Router.navigate("/pages/auth/signIn.js");
  }

  // -----------------------------------------------------------
  // 2. CLIENT-SIDE ROUTER
  // -----------------------------------------------------------
  const routes = {
    "/pages/auth/signIn.js": () => window.SignInPage && window.SignInPage.render(getContainer()),
    "/pages/auth/signUp.js": () => window.SignUpPage && window.SignUpPage.render(getContainer()),
    "/pages/dahsboard/staff.js": () => window.StaffDashboardPage && window.StaffDashboardPage.render(getContainer()),
    "/pages/dahsboard/customer.js": () => window.CustomerDashboardPage && window.CustomerDashboardPage.render(getContainer()),
    "/pages/ocrService.js": () => window.OcrServicePage && window.OcrServicePage.render(getContainer()),
    // Friendly Aliases
    "/signin": () => window.SignInPage && window.SignInPage.render(getContainer()),
    "/signup": () => window.SignUpPage && window.SignUpPage.render(getContainer()),
    "/dashboard/staff": () => window.StaffDashboardPage && window.StaffDashboardPage.render(getContainer()),
    "/dashboard/customer": () => window.CustomerDashboardPage && window.CustomerDashboardPage.render(getContainer()),
    "/ocr": () => window.OcrServicePage && window.OcrServicePage.render(getContainer())
  };

  function getContainer() {
    return document.getElementById("app-root");
  }

  function normalizeRoute(path) {
    if (!path || path === "/" || path === "#" || path === "#/") {
      const token = localStorage.getItem("jwt_token");
      const userType = localStorage.getItem("user_type");
      if (token && userType === "staff") return "/pages/dahsboard/staff.js";
      if (token && userType === "customer") return "/pages/dahsboard/customer.js";
      return "/pages/auth/signIn.js";
    }

    if (path.startsWith("#")) {
      path = path.slice(1);
    }
    return path;
  }

  function navigate(path) {
    const targetRoute = normalizeRoute(path);
    window.location.hash = targetRoute;
    renderCurrentRoute(targetRoute);
  }

  function renderCurrentRoute(routePath) {
    const route = routePath || normalizeRoute(window.location.hash);
    const handler = routes[route];

    if (handler) {
      handler();
    } else {
      // Default fallback
      const token = localStorage.getItem("jwt_token");
      const userType = localStorage.getItem("user_type");
      if (token && userType === "staff") {
        routes["/pages/dahsboard/staff.js"]();
      } else if (token && userType === "customer") {
        routes["/pages/dahsboard/customer.js"]();
      } else {
        routes["/pages/auth/signIn.js"]();
      }
    }

    // Manage inactivity timer depending on whether user is logged in
    const token = localStorage.getItem("jwt_token");
    if (token && (route.includes("dahsboard") || route.includes("dashboard") || route.includes("ocr"))) {
      startIdleTracker();
    } else {
      stopIdleTracker();
    }
  }

  function signOut(message = "Signed out.") {
    stopIdleTracker();
    localStorage.removeItem("jwt_token");
    localStorage.removeItem("user_type");
    localStorage.removeItem("user_email");
    localStorage.removeItem("user_info");
    if (message) {
      console.log(message);
    }
    navigate("/pages/auth/signIn.js");
  }

  // Expose global Router API
  window.Router = {
    navigate,
    signOut,
    resetIdleTimer
  };

  // Initialize on DOM load
  window.addEventListener("DOMContentLoaded", () => {
    window.addEventListener("hashchange", () => {
      renderCurrentRoute(normalizeRoute(window.location.hash));
    });
    renderCurrentRoute();
  });
})();


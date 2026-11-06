/**
 * Gemini Invoice OCR Service Component (Vanilla JavaScript)
 * For staff members to upload invoices, extract text with Gemini, and copy-paste.
 */
function renderOcrService(container) {
  const token = localStorage.getItem("jwt_token");
  const userType = localStorage.getItem("user_type");
  const userEmail = localStorage.getItem("user_email") || "Staff";

  // Check Staff authorization
  if (!token || userType !== "staff") {
    alert("Unauthorized access. OCR service is reserved for staff members.");
    window.Router.navigate("/pages/auth/signIn.js");
    return;
  }

  container.innerHTML = `
    <div class="dashboard-container ocr-container">
      <header class="dashboard-header">
        <div class="user-info">
          <button id="ocr-back-to-dashboard" class="btn btn-secondary btn-small">← Staff Portal</button>
          <h2>Gemini AI Invoice OCR</h2>
          <span class="badge badge-staff">STAFF TOOL</span>
        </div>
        <div class="header-actions">
          <div class="idle-timer-box" title="User activity resets this timer">
            ⏱ Inactivity Timeout: <span id="idle-countdown-display" class="countdown-highlight">120s</span>
          </div>
          <button id="ocr-signout-btn" class="btn btn-secondary">Sign Out</button>
        </div>
      </header>

      <section class="session-notice">
        <p>🤖 <strong>Powered by Google Gemini:</strong> Upload any invoice image (JPG, PNG, WEBP) or document. Gemini will extract vendor details, line items, taxes, and totals for instant copy-pasting.</p>
      </section>

      <div id="ocr-alert" class="alert hidden"></div>

      <!-- Upload Zone -->
      <div class="ocr-grid">
        <div class="ocr-upload-card">
          <h3>1. Upload Invoice</h3>
          <p class="subtitle">Drag & drop or select an invoice file</p>

          <div id="drop-zone" class="drop-zone">
            <div class="drop-zone-icon">📄</div>
            <p class="drop-zone-text"><strong>Click to browse</strong> or drag & drop invoice image</p>
            <p class="drop-zone-subtext">Supports PNG, JPG, JPEG, WEBP, PDF (max 10MB)</p>
            <input type="file" id="file-input" accept="image/*,.pdf" class="file-input-hidden" />
          </div>

          <!-- Selected File Preview -->
          <div id="file-preview-card" class="file-preview-card hidden">
            <div class="file-info-header">
              <span class="file-icon">🖼️</span>
              <div class="file-meta">
                <p id="preview-filename" class="preview-filename">invoice.jpg</p>
                <p id="preview-filesize" class="preview-filesize">0 KB</p>
              </div>
              <button id="remove-file-btn" class="btn-icon" title="Remove file">✕</button>
            </div>
            <div class="thumbnail-wrapper">
              <img id="image-preview" src="" alt="Invoice Preview" class="image-preview" />
            </div>
            <button id="start-ocr-btn" class="btn btn-primary btn-block">
              <span class="btn-text">⚡ Extract Invoice with Gemini</span>
              <span class="btn-spinner hidden"></span>
            </button>
          </div>
        </div>

        <!-- Result / Copy-Paste Zone -->
        <div class="ocr-result-card">
          <div class="result-header">
            <div>
              <h3>2. Extracted Data</h3>
              <p class="subtitle" id="result-status-subtitle">Ready to extract text</p>
            </div>
            <div class="result-actions">
              <button id="copy-text-btn" class="btn btn-success btn-small" disabled>
                <span id="copy-btn-label">📋 Copy to Clipboard</span>
              </button>
              <button id="clear-results-btn" class="btn btn-secondary btn-small" disabled>Clear</button>
            </div>
          </div>

          <div id="ocr-loading-state" class="loading-state hidden">
            <div class="spinner"></div>
            <p id="ocr-progress-msg">Analyzing invoice with Gemini AI model...</p>
          </div>

          <div id="ocr-empty-state" class="empty-state">
            <div class="empty-state-icon">📋</div>
            <p>Upload an invoice on the left to view the extracted details here.</p>
            <small class="text-muted">You will be able to copy the extracted text with a single click.</small>
          </div>

          <div id="ocr-result-wrapper" class="ocr-result-wrapper hidden">
            <textarea id="extracted-text-area" class="extracted-text-area" rows="18" spellcheck="false" placeholder="Extracted invoice data will appear here..."></textarea>
            <div class="result-footer">
              <span id="char-count-badge" class="badge">0 characters</span>
              <span id="engine-badge" class="badge badge-staff">Gemini AI</span>
            </div>
          </div>
        </div>
      </div>
    </div>
  `;

  // Attach Styles dynamically if not already added
  ensureOcrStyles();

  // Elements
  const dropZone = document.getElementById("drop-zone");
  const fileInput = document.getElementById("file-input");
  const previewCard = document.getElementById("file-preview-card");
  const previewImg = document.getElementById("image-preview");
  const previewName = document.getElementById("preview-filename");
  const previewSize = document.getElementById("preview-filesize");
  const removeFileBtn = document.getElementById("remove-file-btn");
  const startOcrBtn = document.getElementById("start-ocr-btn");
  const copyBtn = document.getElementById("copy-text-btn");
  const copyBtnLabel = document.getElementById("copy-btn-label");
  const clearBtn = document.getElementById("clear-results-btn");
  const resultWrapper = document.getElementById("ocr-result-wrapper");
  const emptyState = document.getElementById("ocr-empty-state");
  const loadingState = document.getElementById("ocr-loading-state");
  const textArea = document.getElementById("extracted-text-area");
  const charCountBadge = document.getElementById("char-count-badge");
  const engineBadge = document.getElementById("engine-badge");
  const statusSubtitle = document.getElementById("result-status-subtitle");
  const alertBox = document.getElementById("ocr-alert");

  let currentFile = null;
  let currentBase64 = null;

  // Header Navigations
  document.getElementById("ocr-back-to-dashboard").addEventListener("click", () => {
    window.Router.navigate("/pages/dahsboard/staff.js");
  });

  document.getElementById("ocr-signout-btn").addEventListener("click", () => {
    window.Router.signOut("Staff signed out.");
  });

  // Drag and drop events
  dropZone.addEventListener("click", () => fileInput.click());

  dropZone.addEventListener("dragover", (e) => {
    e.preventDefault();
    dropZone.classList.add("drop-zone-active");
  });

  dropZone.addEventListener("dragleave", () => {
    dropZone.classList.remove("drop-zone-active");
  });

  dropZone.addEventListener("drop", (e) => {
    e.preventDefault();
    dropZone.classList.remove("drop-zone-active");
    if (e.dataTransfer.files && e.dataTransfer.files.length > 0) {
      handleFileSelected(e.dataTransfer.files[0]);
    }
  });

  fileInput.addEventListener("change", () => {
    if (fileInput.files && fileInput.files.length > 0) {
      handleFileSelected(fileInput.files[0]);
    }
  });

  removeFileBtn.addEventListener("click", () => {
    resetUpload();
  });

  clearBtn.addEventListener("click", () => {
    clearResults();
  });

  // Copy to clipboard functionality
  copyBtn.addEventListener("click", async () => {
    const textToCopy = textArea.value;
    if (!textToCopy) return;

    try {
      await navigator.clipboard.writeText(textToCopy);
      copyBtnLabel.textContent = "✅ Copied!";
      copyBtn.classList.add("btn-copied");
      setTimeout(() => {
        copyBtnLabel.textContent = "📋 Copy to Clipboard";
        copyBtn.classList.remove("btn-copied");
      }, 2000);
    } catch (err) {
      // Fallback for older browsers
      textArea.select();
      document.execCommand("copy");
      copyBtnLabel.textContent = "✅ Copied!";
      setTimeout(() => {
        copyBtnLabel.textContent = "📋 Copy to Clipboard";
      }, 2000);
    }
  });

  // Handle selected file
  function handleFileSelected(file) {
    if (!file.type.startsWith("image/") && file.type !== "application/pdf") {
      showAlert("Please upload a valid image file (PNG, JPG, WEBP) or PDF.", "error");
      return;
    }

    if (file.size > 10 * 1024 * 1024) {
      showAlert("File size exceeds 10MB limit. Please choose a smaller file.", "error");
      return;
    }

    hideAlert();
    currentFile = file;
    previewName.textContent = file.name;
    previewSize.textContent = formatBytes(file.size);

    const reader = new FileReader();
    reader.onload = (e) => {
      const dataUrl = e.target.result;
      currentBase64 = dataUrl.split(",")[1];
      if (file.type.startsWith("image/")) {
        previewImg.src = dataUrl;
        previewImg.classList.remove("hidden");
      } else {
        previewImg.classList.add("hidden");
      }
      dropZone.classList.add("hidden");
      previewCard.classList.remove("hidden");
    };
    reader.readAsDataURL(file);
  }

  function resetUpload() {
    currentFile = null;
    currentBase64 = null;
    fileInput.value = "";
    previewImg.src = "";
    dropZone.classList.remove("hidden");
    previewCard.classList.add("hidden");
    hideAlert();
  }

  function clearResults() {
    textArea.value = "";
    resultWrapper.classList.add("hidden");
    emptyState.classList.remove("hidden");
    copyBtn.disabled = true;
    clearBtn.disabled = true;
    statusSubtitle.textContent = "Ready to extract text";
  }

  // Trigger Gemini OCR
  startOcrBtn.addEventListener("click", async () => {
    if (!currentBase64) {
      showAlert("No invoice file loaded.", "error");
      return;
    }

    setOcrLoading(true);
    hideAlert();

    try {
      const response = await fetch("/api/ocr/extract", {
        method: "POST",
        headers: {
          "Content-Type": "application/json",
          "Authorization": `Bearer ${token}`
        },
        body: JSON.stringify({
          image_base64: currentBase64,
          mime_type: currentFile.type || "image/jpeg",
          filename: currentFile.name
        })
      });

      const data = await response.json();

      if (!response.ok || !data.success) {
        if (response.status === 401) {
          window.Router.signOut("Session expired. Please sign in again.");
          return;
        }
        throw new Error(data.error || "OCR extraction failed");
      }

      // Display result
      textArea.value = data.extracted_text;
      charCountBadge.textContent = `${data.extracted_length || data.extracted_text.length} characters`;
      engineBadge.textContent = data.engine || "Gemini Flash";

      emptyState.classList.add("hidden");
      resultWrapper.classList.remove("hidden");
      copyBtn.disabled = false;
      clearBtn.disabled = false;
      statusSubtitle.textContent = `Extracted from "${data.filename}" successfully`;

      showAlert("OCR completed successfully! You can now copy and paste the text below.", "success");

    } catch (err) {
      showAlert("OCR Error: " + err.message, "error");
    } finally {
      setOcrLoading(false);
    }
  });

  function setOcrLoading(isLoading) {
    if (isLoading) {
      startOcrBtn.disabled = true;
      startOcrBtn.querySelector(".btn-text").textContent = "Gemini Processing...";
      startOcrBtn.querySelector(".btn-spinner").classList.remove("hidden");
      emptyState.classList.add("hidden");
      resultWrapper.classList.add("hidden");
      loadingState.classList.remove("hidden");
      copyBtn.disabled = true;
      statusSubtitle.textContent = "Gemini is analyzing document structure...";
    } else {
      startOcrBtn.disabled = false;
      startOcrBtn.querySelector(".btn-text").textContent = "⚡ Extract Invoice with Gemini";
      startOcrBtn.querySelector(".btn-spinner").classList.add("hidden");
      loadingState.classList.add("hidden");
    }
  }

  function showAlert(msg, type) {
    alertBox.textContent = msg;
    alertBox.className = `alert alert-${type}`;
    alertBox.classList.remove("hidden");
  }

  function hideAlert() {
    alertBox.classList.add("hidden");
  }

  function formatBytes(bytes) {
    if (bytes === 0) return "0 Bytes";
    const k = 1024;
    const sizes = ["Bytes", "KB", "MB", "GB"];
    const i = Math.floor(Math.log(bytes) / Math.log(k));
    return parseFloat((bytes / Math.pow(k, i)).toFixed(2)) + " " + sizes[i];
  }
}

function ensureOcrStyles() {
  if (document.getElementById("ocr-custom-styles")) return;
  const style = document.createElement("style");
  style.id = "ocr-custom-styles";
  style.textContent = `
    .ocr-container { max-width: 1050px; }
    .ocr-grid {
      display: grid;
      grid-template-columns: 1fr 1fr;
      gap: 1.5rem;
      margin-top: 1rem;
    }
    @media (max-width: 768px) {
      .ocr-grid { grid-template-columns: 1fr; }
    }
    .ocr-upload-card, .ocr-result-card {
      background: #0f172a;
      border: 1px solid var(--card-border);
      border-radius: 8px;
      padding: 1.5rem;
      display: flex;
      flex-direction: column;
    }
    .drop-zone {
      border: 2px dashed var(--card-border);
      border-radius: 8px;
      padding: 2.5rem 1.5rem;
      text-align: center;
      cursor: pointer;
      margin: 1.25rem 0;
      transition: all 0.2s ease;
      background: rgba(30, 41, 59, 0.4);
    }
    .drop-zone:hover, .drop-zone-active {
      border-color: var(--primary);
      background: rgba(56, 189, 248, 0.05);
    }
    .drop-zone-icon { font-size: 3rem; margin-bottom: 0.5rem; }
    .drop-zone-text { font-size: 0.95rem; margin-bottom: 0.25rem; }
    .drop-zone-subtext { font-size: 0.75rem; color: var(--text-muted); }
    .file-input-hidden { display: none; }
    
    .file-preview-card {
      margin-top: 1rem;
      display: flex;
      flex-direction: column;
      gap: 1rem;
    }
    .file-info-header {
      display: flex;
      align-items: center;
      gap: 0.75rem;
      background: var(--card-bg);
      padding: 0.75rem;
      border-radius: 6px;
      border: 1px solid var(--card-border);
    }
    .file-meta { flex: 1; overflow: hidden; }
    .preview-filename { font-weight: 600; font-size: 0.85rem; text-overflow: ellipsis; white-space: nowrap; overflow: hidden; }
    .preview-filesize { font-size: 0.75rem; color: var(--text-muted); }
    .btn-icon { background: transparent; border: none; color: var(--text-muted); cursor: pointer; font-size: 1rem; padding: 4px 8px; }
    .btn-icon:hover { color: var(--danger); }
    .thumbnail-wrapper {
      max-height: 220px;
      overflow: hidden;
      border-radius: 6px;
      border: 1px solid var(--card-border);
      display: flex;
      align-items: center;
      justify-content: center;
      background: #000;
    }
    .image-preview { max-width: 100%; max-height: 220px; object-fit: contain; }
    .btn-block { width: 100%; }

    .result-header {
      display: flex;
      justify-content: space-between;
      align-items: center;
      margin-bottom: 1rem;
      flex-wrap: wrap;
      gap: 0.5rem;
    }
    .result-actions { display: flex; gap: 0.5rem; }
    .btn-success { background-color: var(--success); color: #fff; }
    .btn-success:hover { background-color: #059669; }
    .btn-copied { background-color: #047857 !important; }
    
    .empty-state {
      flex: 1;
      display: flex;
      flex-direction: column;
      align-items: center;
      justify-content: center;
      padding: 3rem 1.5rem;
      text-align: center;
      color: var(--text-muted);
      border: 1px dashed var(--card-border);
      border-radius: 6px;
    }
    .empty-state-icon { font-size: 2.5rem; margin-bottom: 0.5rem; opacity: 0.6; }

    .ocr-result-wrapper {
      display: flex;
      flex-direction: column;
      flex: 1;
      gap: 0.75rem;
    }
    .extracted-text-area {
      width: 100%;
      background: #020617;
      color: #e2e8f0;
      border: 1px solid var(--card-border);
      border-radius: 6px;
      padding: 1rem;
      font-family: Consolas, Monaco, "Courier New", monospace;
      font-size: 0.88rem;
      line-height: 1.5;
      resize: vertical;
      min-height: 280px;
      outline: none;
    }
    .extracted-text-area:focus { border-color: var(--primary); }
    .result-footer {
      display: flex;
      justify-content: space-between;
      align-items: center;
      font-size: 0.8rem;
    }
  `;
  document.head.appendChild(style);
}

window.OcrServicePage = { render: renderOcrService };


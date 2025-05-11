// main.js
document.getElementById('action-select').addEventListener('change', function() {
    const formatField = document.getElementById('format-group');
    formatField.style.display = this.value === 'convert' ? 'block' : 'none';
});

// Initialize format field visibility
document.addEventListener('DOMContentLoaded', () => {
    const actionSelect = document.getElementById('action-select');
    const formatGroup = document.getElementById('format-group');
    formatGroup.style.display = actionSelect.value === 'convert' ? 'block' : 'none';
});
// main.js - Add these new functions
function initFileInput() {
    const fileInput = document.querySelector('input[type="file"]');
    if (fileInput) {
        fileInput.addEventListener('change', function(e) {
            const fileName = this.files[0]?.name || 'No file selected';
            document.querySelector('.file-status').textContent = fileName;
        });
    }
}

document.addEventListener('DOMContentLoaded', () => {
    initFileInput();
    // Existing initialization code
});
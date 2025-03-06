document.addEventListener('DOMContentLoaded', function() {
    // Show result box with animation if it exists
    const resultBox = document.getElementById('resultBox');
    if (resultBox) {
        setTimeout(() => {
            resultBox.style.display = 'flex';
        }, 100);
    }

    // Reset button functionality
    document.getElementById('resetBtn').addEventListener('click', function() {
        document.getElementById('emailContent').value = '';
        if (resultBox) {
            resultBox.style.display = 'none';
        }
        // Focus on the textarea
        document.getElementById('emailContent').focus();
    });

    // Add loading state to submit button
    document.getElementById('emailForm').addEventListener('submit', function() {
        const button = document.getElementById('predictBtn');
        button.innerHTML = '<span class="spinner-border spinner-border-sm" role="status" aria-hidden="true"></span> Analyzing...';
        button.disabled = true;
    });

    // Character counter for textarea
    const emailContent = document.getElementById('emailContent');
    emailContent.addEventListener('input', function() {
        // Count words
        const wordCount = this.value.trim() ? this.value.trim().split(/\s+/).length : 0;

        // Optional: Display word count somewhere (you can add an element for this)
        console.log('Word count:', wordCount);
    });
});
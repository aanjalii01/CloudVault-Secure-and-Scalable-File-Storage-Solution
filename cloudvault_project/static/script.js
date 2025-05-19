document.addEventListener("DOMContentLoaded", function () {
    const uploadForm = document.getElementById("uploadForm");
    if (uploadForm) {
        uploadForm.addEventListener("submit", function (e) {
            const fileInput = uploadForm.querySelector("input[type='file']");
            if (!fileInput.value) {
                e.preventDefault();
                alert("Please choose a file to upload.");
            }
        });
    }
});

// Optional JavaScript for progress bar or other features
document.addEventListener("DOMContentLoaded", function () {
    const uploadForm = document.getElementById("uploadForm");
    const progressBar = document.getElementById("progressBar");

    if (uploadForm) {
        uploadForm.addEventListener("submit", function (e) {
            e.preventDefault();
            const formData = new FormData(uploadForm);
            const xhr = new XMLHttpRequest();
            xhr.open("POST", "/upload", true);

            xhr.upload.onprogress = function (e) {
                if (e.lengthComputable) {
                    const percent = (e.loaded / e.total) * 100;
                    progressBar.value = percent;
                }
            };

            xhr.onload = function () {
                if (xhr.status === 200) {
                    alert("Upload successful!");
                    window.location.reload();  // Reload to show new file
                } else {
                    alert("Upload failed.");
                }
            };

            xhr.send(formData);
        });
    }
});

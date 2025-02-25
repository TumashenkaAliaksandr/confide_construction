document.getElementById("add-photo-btn").addEventListener("click", function () {
    document.getElementById("photo-input").click();
});

document.getElementById("photo-input").addEventListener("change", function () {
    let photoList = document.getElementById("photo-list");
    let countDisplay = document.getElementById("photo-count");
    let maxFiles = 10;
    let maxSize = 5 * 1024 * 1024; // 5MB
    let allowedTypes = ["image/jpeg", "image/png", "image/gif"];

    let currentFiles = photoList.getElementsByTagName("li").length;

    if (currentFiles >= maxFiles) {
        alert("You can upload up to 10 photos only.");
        return;
    }

    for (let file of this.files) {
        if (currentFiles >= maxFiles) break;

        if (!allowedTypes.includes(file.type)) {
            alert("Invalid file type: " + file.name);
            continue;
        }
        if (file.size > maxSize) {
            alert("File too large: " + file.name);
            continue;
        }

        let listItem = document.createElement("li");
        listItem.textContent = file.name + " ";

        let removeBtn = document.createElement("button");
        removeBtn.textContent = "❌";
        removeBtn.style.marginLeft = "7px";
        removeBtn.addEventListener("click", function () {
            listItem.remove();
            countDisplay.textContent = "Uploaded photos: " + photoList.getElementsByTagName("li").length;
        });

        listItem.appendChild(removeBtn);
        photoList.appendChild(listItem);
        currentFiles++;
    }

    countDisplay.textContent = "Uploaded photos: " + photoList.getElementsByTagName("li").length;
    this.value = ""; // Очищаем input, чтобы можно было повторно выбрать те же файлы
});

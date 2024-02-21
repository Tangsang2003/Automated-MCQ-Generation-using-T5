function autoResize() {
    var textarea = document.getElementById("paragraphs");
    var maxHeight = 500;  // Set your desired maximum height here

    textarea.style.height = "auto";
    textarea.style.height = Math.min(textarea.scrollHeight, maxHeight) + "px";
}

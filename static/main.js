function autoResize() {
    var textarea = document.getElementById("paragraphs");
    var maxHeight = 500;  // Set your desired maximum height here

    textarea.style.height = "auto";
    textarea.style.height = Math.min(textarea.scrollHeight, maxHeight) + "px";
}

function checkAnswer(selectedOption) {
        const optionsList = selectedOption.parentNode;
        const correctAnswer = optionsList.getAttribute('data-correct-answer');
        const allOptions = optionsList.getElementsByTagName('li');

        // Reset styles for all options
        for (let i = 0; i < allOptions.length; i++) {
            allOptions[i].classList.remove('selected-option-correct', 'selected-option-incorrect');
        }

        // Check if the selected option is correct
        if (selectedOption.textContent === correctAnswer) {
            selectedOption.classList.add('selected-option-correct');
        } else {
            selectedOption.classList.add('selected-option-incorrect');
        }

        // Display correct answer
        const correctAnswerElement = optionsList.nextElementSibling;
        correctAnswerElement.style.display = 'block';
        }
// loader

function hideLoader(){
//  $('.page-loader-2').fadeOut('slow');
  $('.page-loader-2').hide();
  $('.page-loader').fadeOut('slow');
}

function hideLoader_two(){
//  $('.page-loader').fadeOut('slow');
//  $('.page-loader-2').fadeOut('slow');
    $('.page-loader').hide();
    $('.page-loader-2').fadeOut('slow');
}

 function showLoader() {
            // Show the loader
            $('.page-loader-2').fadeIn('slow');
 }

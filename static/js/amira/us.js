function getRandomSentence() {
    const sentencePlaceholder = document.getElementById('sentence-placeholder');
    sentencePlaceholder.style.opacity = 0;

    fetch('https://winstonsarchive-production.up.railway.app/amira/api/sentences')
        .then(response => response.json())
        .then(data => {
            const randomIndex = Math.floor(Math.random() * data.length);
            const randomSentence = data[randomIndex].sentence;

            sentencePlaceholder.innerText = randomSentence;
            sentencePlaceholder.style.opacity = 1;
        })
        .catch(error => console.error('Error fetching data:', error));
}

function calculateTimeDifference() {
    const startDate = new Date('December 19, 2022 00:00:00 GMT');
    const currentDate = new Date('July 13, 2024 13:31:00 GMT');
    const timeDifference = currentDate - startDate;

    const seconds = Math.floor(timeDifference / 1000);
    const minutes = Math.floor(seconds / 60);
    const hours = Math.floor(minutes / 60);
    const days = Math.floor(hours / 24);

    return {
        days: days,
        hours: hours % 24,
        minutes: minutes % 60,
        seconds: seconds % 60
    };
}

function updateCounter() {
    const counterElement = document.getElementById('counter');

    function update() {
        const time = calculateTimeDifference();
        counterElement.innerHTML = `${time.days} days ${time.hours} hours ${time.minutes} minutes ${time.seconds} seconds`;
    }

    update();
    setInterval(update, 1000);
}

function enlargeImage(image) {
    const enlargedImage = document.querySelector('.enlarged-image');
    const clone = image.cloneNode(true);
    enlargedImage.innerHTML = '';
    enlargedImage.appendChild(clone);
    clone.style.filter = 'None';
    enlargedImage.style.display = 'flex';

    enlargedImage.addEventListener('click', () => {
        enlargedImage.style.display = 'none';
    });
}

function filterImages(month) {
    const hiddenImages = document.querySelectorAll('.hidden-images');
    hiddenImages.forEach(element => {
        element.style.display = 'none';
    });

    const enlargedImage = document.querySelector('.enlarged-image');
    enlargedImage.style.display = 'none';

    const selectedImages = document.getElementById(month);
    if (selectedImages) {
        selectedImages.style.display = 'block';
    }

    const enlargeImages = selectedImages.querySelectorAll('.enlarge-image');
    enlargeImages.forEach(image => {
        image.addEventListener('click', () => {
            enlargeImage(image);
        });
    });
}

document.addEventListener('DOMContentLoaded', function () {
    updateCounter();

    const enlargedImage = document.createElement('div');
    enlargedImage.className = 'enlarged-image';
    document.body.appendChild(enlargedImage);

    const filterButtons = document.querySelectorAll('.filter-button');
    filterButtons.forEach(button => {
        button.addEventListener('click', () => {
            const month = button.getAttribute('data-month');
            filterImages(month);
        });
    });

    const initialMonth = 'default';
    filterImages(initialMonth);
});
window.onload = function() {
    const yesBtn = document.getElementById('yes-btn');
    const noBtn = document.getElementById('no-btn');
    const valentineGif = document.getElementById('valentine-gif');
    const valentinesText = document.getElementById('valentines-text');
    const wrapper = document.querySelector('.wrapper');

    const noBtnActions = [
        {
            gif: "{% static 'css/amira/imgs/sad1.gif' %}",
            text: "why not? :("
        },
        {
            gif: "{% static 'css/amira/imgs/sad2.gif' %}",
            text: "but... i really want to :("
        },
        {
            gif: "{% static 'css/amira/imgs/sad3.gif' %}",
            text: "don't make me cry :("
        },
        {
            gif: "{% static 'css/amira/imgs/no-choice.gif' %}",
            text: "you are not allowed to say no to me ☺️",
            hideNoBtn: true
        }
    ];

    let noBtnClickCount = 0;

    noBtn.addEventListener('click', function () {
        if (noBtnClickCount < noBtnActions.length) {
            const action = noBtnActions[noBtnClickCount];
            valentineGif.src = action.gif;
            valentinesText.innerText = action.text;
            if (action.hideNoBtn) {
                noBtn.style.display = 'none';
            }
        }

        // Reallocate no-btn
        const randomX = Math.floor(Math.random() * (wrapper.offsetWidth - noBtn.offsetWidth));
        const randomY = Math.floor(Math.random() * (wrapper.offsetHeight - noBtn.offsetHeight));
        noBtn.style.left = randomX + 'px';
        noBtn.style.top = randomY + 'px';

        // Make yes-btn bigger
        var old_font_size = parseInt(yesBtn.style.fontSize) || 0;
        var old_width = yesBtn.offsetWidth;
        var old_height = yesBtn.offsetHeight;
        yesBtn.style.fontSize = (old_font_size + 60) + 'px';
        yesBtn.style.width = (old_width + 100) + 'px';
        yesBtn.style.height = (old_height + 100) + 'px';

        noBtnClickCount++;
    });

    yesBtn.addEventListener('click', function () {
        valentineGif.src = "{% static 'css/amira/imgs/yes.gif' %}";
        valentinesText.innerText = "😁😁😁😁 te amo!! 😁😁😁😁";
        yesBtn.style.display = 'none';
        noBtn.style.display = 'none';
    });

    // Set the initial left and top of no-btn to be next to yes-btn
    noBtn.style.display = 'none';
    noBtn.style.left = (yesBtn.offsetLeft + yesBtn.offsetWidth) + 'px';
    noBtn.style.top = yesBtn.offsetTop + 'px';
    noBtn.style.display = 'block';
};
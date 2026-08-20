console.log("Custom - Done")
frappe.after_ajax(() => {

    $("body").append(`
        <button id="play"
            style="
                position: fixed;
                bottom: 20px;
                right: 20px;
                z-index: 9999;
                padding: 10px 20px;
                background: #0d6efd;
                color: white;
                border: none;
                border-radius: 6px;
                cursor: pointer;">
            ▶ Play Music
        </button>
    `);

    $("#play").click(function () {

        const music = $("#sound-ping")[0];

        if (!music) {
            console.log("Audio element not found");
            return;
        }

        if (music.paused) {
            music.play();
            $(this).text("⏸ Pause Music");
        } else {
            music.pause();
            $(this).text("▶ Play Music");
        }

    });

});
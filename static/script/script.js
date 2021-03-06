var player;

function onYouTubeIframeAPIReady() {
    player = new YT.Player('video-placeholder', {
        width: 600,
        height: 400,
        videoId: '0JUN9aDxVmI',
        playerVars: {
            color: 'white',
            playlist: 'taJ60kskkns,FG0fTKAqZ5g'
        },
        events: {
            onReady: initialize
        }
    });
}

function initialize(){

// Update the controls on load
updateTimerDisplay();
updateProgressBar();

// Clear any old interval.
clearInterval(time_update_interval);

// Start interval to update elapsed time display and
// the elapsed part of the progress bar every second.
time_update_interval = setInterval(function () {
    updateTimerDisplay();
    updateProgressBar();
}, 1000)

}

// This function is called by initialize()
function updateTimerDisplay(){
    // Update current time text display.
    $('#current-time').text(formatTime( player.getCurrentTime() ));
    $('#duration').text(formatTime( player.getDuration() ));
}

function formatTime(time){
    time = Math.round(time);

    var minutes = Math.floor(time / 60),
    seconds = time - minutes * 60;

    seconds = seconds < 10 ? '0' + seconds : seconds;
    console.log(seconds)
    return minutes + ":" + seconds;
}

function returnTime(){

    var x = formatTime( player.getCurrentTime());
    alert("Got it at " + x);
}

function returnTime2(){

    var x = formatTime( player.getCurrentTime());
    alert("Didn't understand at " + x);
}




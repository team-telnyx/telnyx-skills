$(document).ready(function() {
    var audioElements = $('audio.voice-response');
    var playButtons = $('i.play-icon');

    _.each(_.zip(playButtons, audioElements), function(playPair) {
        $(playPair[0]).click(function() {
            playPair[1].play();
        });
    });
});

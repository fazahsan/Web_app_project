document.addEventListener("DOMContentLoaded", function() {
    if (annyang) {
        // Define commands
        var commands = {
            'turn on *appliance': function(appliance) {
                handleCommand(appliance, true);
            },
            'turn off *appliance': function(appliance) {
                handleCommand(appliance, false);
            }
        };

        // Add commands to annyang
        annyang.addCommands(commands);

        // Start listening
        annyang.start();
    }

    function handleCommand(appliance, turnOn) {
        // Find the corresponding appliance element
        var applianceElement = document.querySelector(`[data-name="${appliance.toLowerCase()}"]`);
        if (applianceElement) {
            // Find the form inside the appliance element
            var form = applianceElement.querySelector('form');
            var statusElement = applianceElement.querySelector('.status');
            var bulbElement = applianceElement.querySelector('.light-bulb');
            var refElement = applianceElement.querySelector('.light-indicator');

            // Change the button text based on the command
            var button = form.querySelector('button');
            button.innerHTML = turnOn ? 'Turn Off' : 'Turn On';

            // Change the status text
            statusElement.innerHTML = 'Status: ' + (turnOn ? 'On' : 'Off');

            // Update the bulb class
            if (bulbElement) {
                bulbElement.classList.toggle('on', turnOn);
                bulbElement.classList.toggle('off', !turnOn);
            }

            if (refElement) {
                refElement.classList.toggle('on', turnOn);
                refElement.classList.toggle('off', !turnOn);
            }

            // Submit the form
            form.submit();
        }
    }
});

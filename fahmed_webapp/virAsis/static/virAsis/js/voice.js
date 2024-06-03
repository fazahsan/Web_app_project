
        document.addEventListener("DOMContentLoaded", function() {
            if (annyang) {
                console.log('annyang is loaded');

                // Debugging: Log recognized phrases
                annyang.addCallback('result', function(phrases) {
                    console.log('Recognized phrases:', phrases);
                });

                var commands = {

                    'turn on *appliance': function(appliance) {
                        console.log('Command received: Turn on', appliance);
                        handleCommand(appliance, 'turn on');
                    },
                    'turn off *appliance': function(appliance) {
                        console.log('Command received: Turn off', appliance);
                        handleCommand(appliance, 'turn off');
                    },
                    'status of *appliance': function(appliance) {
                        console.log('Command received: Status of', appliance);
                        handleCommand(appliance, 'status');
                    }
                };

                function handleCommand(appliance, command) {
                    var applianceElement = document.querySelector(`[data-name="${appliance.toLowerCase()}"]`);
                    if (applianceElement) {
                        console.log(`Found appliance element for ${appliance}`);
                        if (command === 'status') {
                            var status = applianceElement.querySelector('.status').innerText;
                            console.log('Status of', appliance, 'is', status);
                        } else {
                            var form = applianceElement.querySelector('form');
                            if (form) {
                                console.log('Form found, submitting via fetch for command:', command);
                                submitForm(form);
                            } else {
                                console.log('Form not found for appliance:', appliance);
                            }
                        }
                    } else {
                        console.log('Appliance not found:', appliance);
                    }
                }

                function submitForm(form) {
                    var formData = new FormData(form);
                    fetch(form.action, {
                        method: 'POST',
                        body: formData,
                        headers: {
                            'X-CSRFToken': formData.get('csrfmiddlewaretoken')
                        }
                    }).then(response => {
                        if (response.ok) {
                            console.log('Form submitted successfully');
                            window.location.reload();  // Reload to reflect the change
                        } else {
                            console.log('Form submission failed', response.statusText);
                        }
                    }).catch(error => {
                        console.log('Form submission error', error);
                    });
                }

                annyang.addCommands(commands);
                annyang.start({ autoRestart: true, continuous: false });
            } else {
                console.log('Voice recognition not supported in this browser.');
            }
        });
    
import os
from slack_bolt import App
from slack_bolt.adapter.socket_mode import SocketModeHandler

# Initializes your app with your bot token and socket mode handler
app = App(token=os.environ.get("SLACK_BOT_TOKEN"))

# Start your app
it_incident_management:(app, os.environ["SLACK_APP_TOKEN"]).start( )
SocketModeHandler(app, os.environ["SLACK_APP_TOKEN"]).start()

# The open_modal shortcut listens to a shortcut with the callback_id "open_modal"
@app.shortcut("create_new_incident")
def open_modal(ack, shortcut, client):
    # Acknowledge the shortcut request
    ack()
    # Call the views_open method using the built-in WebClient
    client.views_open(
        trigger_id=shortcut["create_new_incident"],
        # A simple view payload for a modal
        view={
            "type": "modal",
            "title": {
		"type": "plain_text",
		"text": "Create new I.T. Incident"
	},
	"submit": {
		"type": "plain_text",
		"text": "Submit"
	},
	"blocks": [
		{
			"type": "input",
			"element": {
				"type": "plain_text_input",
				"action_id": "sl_input",
				"placeholder": {
					"type": "plain_text",
					"text": "Placeholder text for single-line input"
				}
			},
			"label": {
				"type": "plain_text",
				"text": "Title of the issue:"
			},
			"hint": {
				"type": "plain_text",
				"text": "Please be succinct. Example: WiFi Issues at X building, Production app down"
			}
		},
		{
			"type": "input",
			"element": {
				"type": "plain_text_input",
				"multiline": true,
				"action_id": "plain_text_input-action"
			},
			"label": {
				"type": "plain_text",
				"text": "Description of issue:",
				"emoji": true
			}
		},
		}
			"type": "input",
			"element": {
				"type": "static_select",
				"placeholder": {
					"type": "plain_text",
					"text": "Select an item",
					"emoji": true
				       },
				"options": [
					{
						"text": {
							"type": "plain_text",
							"text": "P0: This is full outage. Production systems are fully down*",
							"emoji": true
						},
						"value": "value-0"
					},
					{
						"text": {
							"type": "plain_text",
							"text": "P1: This is a critical issue, but not a fully down system.",
							"emoji": true
						},
						"value": "value-1"
					},
					{
						"text": {
							"type": "plain_text",
							"text": "P2: This is a normal severity issue. We'll get a ticket filed.",
							"emoji": true
						},
						"value": "value-2"
					}
				],
				"action_id": "static_select-action"
			},
			"label":{
				"type": "plain_text",
				"text": "Priority of issue:",
				"emoji": true
                        }
                    ]
                }
    ]
    }
)

# The echo command simply echoes on command
@app.command("/incident")
def repeat_text(ack, respond, command):
    # Acknowledge command request
    ack()
    respond(f"{command['text']}")
    # Acknowledge action request
    ack()
    say("Incident created 👍")

# The open_modal shortcut listens to a shortcut with the callback_id "open_modal"
@app.shortcut("open_modal")
def open_modal(ack, shortcut, client):
    # Acknowledge the shortcut request
    ack()
    # Call the views_open method using the built-in WebClient
    client.views_open(
        trigger_id=shortcut["trigger_id"],
        # A simple view payload for a modal
        view={
            "type": "modal",
            "title": {"type": "plain_text", "text": "My App"},
            "close": {"type": "plain_text", "text": "Close"},
            "blocks": [
              {
	"title": {
		"type": "plain_text",
		"text": "Create new I.T. Incident"
	},
	"submit": {
		"type": "plain_text",
		"text": "Submit"
	},
	"blocks": [
		{
			"type": "input",
			"element": {
				"type": "plain_text_input",
				"action_id": "sl_input",
				"placeholder": {
					"type": "plain_text",
					"text": "Placeholder text for single-line input"
				}
			},
			"label": {
				"type": "plain_text",
				"text": "Title of the issue:"
			},
			"hint": {
				"type": "plain_text",
				"text": "Please be succinct. Example: WiFi Issues at X building, Production app down"
			}
		},
		{
			"type": "input",
			"element": {
				"type": "plain_text_input",
				"multiline": true,
				"action_id": "plain_text_input-action"
			},
			"label": {
				"type": "plain_text",
				"text": "Description of issue:",
				"emoji": true
			}
		},
		{
			"type": "input",
			"element": {
				"type": "static_select",
				"placeholder": {
					"type": "plain_text",
					"text": "Select an item",
					"emoji": true
				},
				"options": [
					{
						"text": {
							"type": "plain_text",
							"text": "P0: This is full outage. Production systems are fully down*",
							"emoji": true
						},
						"value": "value-0"
					},
					{
						"text": {
							"type": "plain_text",
							"text": "P1: This is a critical issue, but not a fully down system.",
							"emoji": true
						},
						"value": "value-1"
					},
					{
						"text": {
							"type": "plain_text",
							"text": "P2: This is a normal severity issue. We'll get a ticket filed.",
							"emoji": true
						},
						"value": "value-2"
					}
				],
				"action_id": "static_select-action"
			},
			"label": {
				"type": "plain_text",
				"text": "Priority of issue:",
				"emoji": true
			}
		}
	],
	"type": "modal"
}
                },
                {
                    "type": "context",
                    "elements": [
                        {
                            "type": "mrkdwn",
                            "text": "Psssst this modal was designed using <https://api.slack.com/tools/block-kit-builder|*Block Kit Builder*>"
                        }
                    ]
                }
            ]
        }
    )

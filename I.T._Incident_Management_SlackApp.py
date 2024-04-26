from slack_bolt import App
from slack_bolt.adapter.socket_mode import SocketModeHandler
import os
from dotenv import load_dotenv

load_dotenv()
SLACK_BOT_TOKEN = os.environ["SLACK_BOT_TOKEN"]
SLACK_APP_TOKEN = os.environ["SLACK_APP_TOKEN"]

app = App(token=os.environ["SLACK_BOT_TOKEN"])

# Listen for an app mention
@app.event("app_mention")                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                      
def mention_handler(body, say):
        say("Hello! If you'd like to create an incident, please use the /incident shortcut")

# Listen for a shortcut invocation
@app.shortcut("create_new_incident")
def open_modal(ack, body, client):
    # Acknowledge the command request
    ack()
    # Call views_open with the built-in client
    client.views_open(
        # Pass a valid trigger_id within 3 seconds of receiving it
        trigger_id=body["trigger_id"],
        # View payload
        view={
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
		)
    		 }
)

if __name__ == "__main__":
    SocketModeHandler(app, os.environ["SLACK_APP_TOKEN"]).start()

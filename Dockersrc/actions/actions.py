from rasa_sdk import Action, Tracker
from rasa_sdk.executor import CollectingDispatcher
from rasa_sdk.events import SlotSet, EventType, ActiveLoop, LoopInterrupted
from rasa_sdk.types import DomainDict
from typing import Any, List, Dict, Text
import random

class RandomResponseAction(Action):
    def name(self) -> Text:
        return "action_random_response"
    
    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        
            random_responses = ["What else would you like to know about?",
                           "Is there anything else I can help you with?",
                           "Would you like to know more about anything else?"]
        
            random_response = random.choice(random_responses)
            dispatcher.utter_message(text=random_response)
            
            return []


#class ProvideInformation(Action):

    # def run(
    #     self,
    #     dispatcher: CollectingDispatcher,
    #     tracker: Tracker,
    #     domain: DomainDict
    # ) -> List[EventType]:
    #     entities = tracker.latest_message['entities']
    #     print("Entities:", entities)
    #     if entities:
    #         feature = next((e for e in entities if e['entity'] == 'feature'), None)
    #         print("Feature:", feature) 
    #         if feature:
    #             feature_name = feature['value']
    #             if feature_name.lower() == "fcr":
    #                 response = "The FCR stands for Field Coaching Report used by Managers to assess end-users. It is found in the Coach Module."
    #             elif feature_name.lower() == "action pack":
    #                 response = "The Action Pack is the main course learning that is built within learning sets. It is where all the training materials are found"
    #             elif feature_name.lower() == "learning set":
    #                 response = "The Learning set is a group of action-packs packed in one module like a learning course, found in the learn module"
    #             elif feature_name.lower() == "resources":
    #                 response = "The Resources is a content hub of any file uploads that are available to you via deployment from the Launchpad. They also come as a collection which is a folder of Resources."
    #             elif feature_name.lower() == "forms":
    #                 response = "The Forms are the main sort of resource files for ACTO specific tasks. For example In Learn Module, Actionpacks can use Quiz, Surveys and Digital signature Forms. Then there are other assessment forms such as Assessment,Evaluation and FCR that are used within Coach tool Certification and Scenarios and FCR"
    #             elif feature_name.lower() == "coach":
    #                 response = "The Coach tool is located under Learn in the application, and has a person icon on it. It is where managers can certify users, assess them, create scenarios for them or field coaching reports, including video submissions."
    #             else:
    #                 response = "There is no feature like that on the platform. Try using key-words from the application like: Learning Report, FCR, Coach etc."
    #             dispatcher.utter_message(response)
    #             # check if the user wants to exit the form
    #             should_exit = tracker.latest_message.get("intent", {}).get("name") == "form_exit"
    #             if should_exit:
    #                 return [SlotSet("form_exit", True), SlotSet("feature", None), ActiveLoop(None)]
    #             else:
    #                 return [SlotSet("feature", None), ActiveLoop("action_provide_information"), LoopInterrupted(False)]
    #     else:
    #         response = "Sorry, I didn't understand if you still want to know about a specific feature. To return to general chat, please type -> Take me to general chat"
    #         dispatcher.utter_message(response)
    #         return [SlotSet("feature", None), ActiveLoop("action_provide_information"), LoopInterrupted(True)]






class ActionAskForMoreInfo(Action):
    def name(self) -> Text:
        return "action_ask_for_more_info"

    def run(
        self, dispatcher: CollectingDispatcher, tracker: Tracker, domain: Dict[Text, Any]
    ) -> List[Dict[Text, Any]]:
        dispatcher.utter_message(template="utter_ask_follow_up")
        return []

class ActionEntityOutOfBounds(Action):
    def name(self) -> Text:
        return "action_entity_out_of_bounds"

    def run(
        self, dispatcher: CollectingDispatcher, tracker: Tracker, domain: Dict[Text, Any]
    ) -> List[Dict[Text, Any]]:
        dispatcher.utter_message(template="utter_default")
        return []

class ActionFAQ(Action):
    def name(self) -> Text:
        return "action_faq"

    def run(
        self, dispatcher: CollectingDispatcher, tracker: Tracker, domain: Dict[Text, Any]
    ) -> List[Dict[Text, Any]]:
        dispatcher.utter_message(template="utter_faq")
        return []

class ActionDeactivateForm(Action):
    def name(self) -> Text:
        return "action_deactivate_form"

    def run(self, tracker: Tracker, dispatcher: CollectingDispatcher, domain: Dict[Text, Any]):
        return [SlotSet("active_loop", None)]

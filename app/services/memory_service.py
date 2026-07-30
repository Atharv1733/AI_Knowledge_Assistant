conversation_history = []


def add_message(role: str, message: str):
    conversation_history.append(
        {
            "role": role,
            "message": message
        }
    )

    print("\nCurrent Memory:")
    for chat in conversation_history:
        print(chat)
    print("-" * 50)


def get_history():

    return conversation_history


def clear_history():

    conversation_history.clear()
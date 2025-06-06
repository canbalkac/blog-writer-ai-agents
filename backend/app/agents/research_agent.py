import wikipedia

def research_topic(topic: str) -> str:
    try:
        summary = wikipedia.summary(topic, sentences=3)
        return summary
    except wikipedia.exceptions.DisambiguationError as e:
        return f"Topic is ambiguous. Try one of: {e.options[:5]}"
    except wikipedia.exceptions.PageError:
        return "No page found for this topic."
    except Exception as e:
        return f"Unexpected error: {str(e)}"
from app.schemas.chat_schema import ChatResponse
from app.services.llm_service import generate_response
from app.services.retriever import retrieve_context


def get_answer(question: str) -> ChatResponse:

    # Retrieve relevant chunks
    retrieved_chunks = retrieve_context(question)

    # Build context
    context = "\n\n".join(
        chunk["text"] for chunk in retrieved_chunks
    )

    # Generate answer
    answer = generate_response(
        question=question,
        context=context
    )

    # Remove duplicate sources
    unique_sources = []
    seen = set()

    for chunk in retrieved_chunks:

        source = (
            chunk["source"],
            chunk["page"]
        )

        if source not in seen:
            seen.add(source)
            unique_sources.append(source)

    source_text = "\n".join(
        f"• {source} (Page {page})"
        for source, page in unique_sources
    )

    if answer.strip() == "I couldn't find this information in the knowledge base.":
        final_answer = answer
    else:
        final_answer = (
            f"{answer}\n\n"
            f"Sources:\n"
            f"{source_text}"
        )


    return ChatResponse(
        answer=final_answer
    )
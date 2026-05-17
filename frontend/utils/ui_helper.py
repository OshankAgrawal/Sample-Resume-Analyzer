import streamlit as st

def display_scores_cards(result):
    st.subheader("Match Scores")

    col1, col2, col3 = st.columns(3)

    col1.metric(
        "Semantic Score",
        f"{result["semantic_match_score"]}%"
    )

    col2.metric(
        "LLM Score",
        f"{result["llm_match_score"]}%"
    )

    col3.metric(
        "Final Score",
        f"{result["final_match_score"]}%"
    )


def display_recommendation(result):
    st.subheader("Recommendation")

    recommendation = result["recommendation"]

    if recommendation == "Shortlist":
        st.success(f"{recommendation}")
    else:
        st.error(f"{recommendation}")


def display_list_section(title, items):

    st.subheader(f"{title}")

    if not items:
        st.write("No data available.")

    else:

        for item in items:
            st.write(f"- {item}")
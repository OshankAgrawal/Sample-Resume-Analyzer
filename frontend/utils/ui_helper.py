import streamlit as st

def display_scores_cards(result):

    st.markdown(
        """
        <h2 style='margin-bottom:30px;'>
            Match Scores
        </h2>
        """,
        unsafe_allow_html=True
    )

    col1, col2, col3 = st.columns(3)

    scores = [
        (
            "Semantic Score",
            result["semantic_match_score"]
        ),
        (
            "LLM Score",
            result["llm_match_score"]
        ),
        (
            "Final Score",
            result["final_match_score"]
        )
    ]

    for col, (title, score) in zip(
        [col1, col2, col3],
        scores
    ):

        col.markdown(
            f"""
            <div class="score-card", style='margin-bottom:30px;'>
                <h3>{title}</h3>
                <h1>{score}%</h1>
            </div>
            """,
            unsafe_allow_html=True
        )


def display_recommendation(result):

    recommendation = result["recommendation"]

    css_class = (
        "shortlist"
        if recommendation == "Shortlist"
        else "reject"
    )

    st.markdown(
        f"""
        <div class="
            recommendation-box {css_class}
        ">
            {recommendation}
        </div>
        """,
        unsafe_allow_html=True
    )


def display_list_section(title, items):

    with st.expander(f"{title}", expanded=False):
        if not items:
            st.write("No data available.")

        else:
            for item in items:
                st.markdown(f"- {item}")
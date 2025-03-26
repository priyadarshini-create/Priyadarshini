import streamlit as st

# Page Title
st.title("🌿 Soil Recommendation Rating Page")

# Rating System
st.subheader("Rate the Recommendations")
rating = st.slider("Select a rating:", min_value=1, max_value=5, value=3)

# Additional Feedback for Low Ratings
reason = ""
if rating < 3:
    st.subheader("We’re sorry to hear that! 😟")
    reason = st.text_area("Could you please tell us why you gave a low rating?")

# Feedback Input
st.subheader("Provide Your Feedback")
feedback = st.text_area("Tell us what you think about the recommendations:")

# Submit Button
if st.button("Submit Feedback"):
    if feedback.strip():
        response = f"Thank you for your feedback! 🌟\n\n**Rating:** {rating}/5\n\n**Feedback:** {feedback}"
        if rating < 3 and reason.strip():
            response += f"\n\n**Reason for Low Rating:** {reason}"
        elif rating < 3:
            st.warning("Please provide a reason for your low rating.")
        else:
            st.success(response)
    else:
        st.warning("Please provide feedback before submitting.")

st.markdown("---")

# Footer
st.caption("Soil Recommendation System © 2025")
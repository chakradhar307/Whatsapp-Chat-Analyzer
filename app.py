
# import streamlit as st 
# import preprocessor, helper 
# import matplotlib.pyplot as plt 
# import seaborn as sns 

# # --- Page Configuration ---
# st.set_page_config(page_title="📊 WhatsApp Chat Analyzer", layout="wide")

# # --- Sidebar ---
# st.sidebar.title("💬 WhatsApp Chat Analyzer")
# uploaded_file = st.sidebar.file_uploader("📂 Upload your chat file")

# # --- Main Layout ---
# st.markdown("<h1 style='text-align: center; color: #4A4A4A;'>📱 WhatsApp Chat Analyzer</h1>", unsafe_allow_html=True)

# if uploaded_file is not None:
#     bytes_data = uploaded_file.getvalue()
#     data = bytes_data.decode("utf-8")
#     df = preprocessor.preprocess(data)

#     user_list = df['user'].unique().tolist()
#     if 'group_notification' in user_list:
#         user_list.remove('group_notification')
#     user_list.sort()
#     user_list.insert(0, "Overall")

#     selected_user = st.sidebar.selectbox("👤 Analyze for", user_list)

#     if st.sidebar.button("🚀 Show Analysis"):

#         # --- Top Statistics ---
#         st.markdown("## 🔢 Top Statistics")
#         num_messages, words, num_media_messages, num_links = helper.fetch_stats(selected_user, df)
#         col1, col2, col3, col4 = st.columns(4)

#         col1.metric("💬 Messages", num_messages)
#         col2.metric("📝 Words", words)
#         col3.metric("📸 Media", num_media_messages)
#         col4.metric("🔗 Links", num_links)

#         st.markdown("---")

#         # --- Timelines ---
#         st.markdown("## 🗓️ Message Timelines")
#         col1, col2 = st.columns(2)

#         with col1:
#             st.markdown("### 📅 Monthly Timeline")
#             timeline = helper.monthly_timeline(selected_user, df)
#             fig, ax = plt.subplots()
#             ax.plot(timeline['time'], timeline['message'], color='green')
#             plt.xticks(rotation=45)
#             st.pyplot(fig)

#         with col2:
#             st.markdown("### 🕘 Daily Timeline")
#             daily_timeline = helper.daily_timeline(selected_user, df)
#             fig, ax = plt.subplots()
#             ax.plot(daily_timeline['only_date'], daily_timeline['message'], color='black')
#             plt.xticks(rotation=45)
#             st.pyplot(fig)

#         st.markdown("---")

#         # --- Activity Maps ---
#         st.markdown("## 📊 Activity Maps")
#         col1, col2 = st.columns(2)

#         with col1:
#             st.markdown("### 📆 Most Busy Day")
#             busy_day = helper.week_activity_map(selected_user, df)
#             fig, ax = plt.subplots()
#             ax.bar(busy_day.index, busy_day.values, color='purple')
#             plt.xticks(rotation=45)
#             st.pyplot(fig)

#         with col2:
#             st.markdown("### 🗓️ Most Busy Month")
#             busy_month = helper.month_activity_map(selected_user, df)
#             fig, ax = plt.subplots()
#             ax.bar(busy_month.index, busy_month.values, color='orange')
#             plt.xticks(rotation=45)
#             st.pyplot(fig)

#         st.markdown("### 🧭 Weekly Heatmap")
#         user_heatmap = helper.activity_heatmap(selected_user, df)
#         fig, ax = plt.subplots()
#         ax = sns.heatmap(user_heatmap, cmap="YlGnBu")
#         st.pyplot(fig)

#         st.markdown("---")

#         # --- Busiest Users (Only for Group Analysis) ---
#         if selected_user == 'Overall':
#             st.markdown("## 🏆 Most Active Users")
#             x, new_df = helper.most_busy_users(df)
#             col1, col2 = st.columns(2)

#             with col1:
#                 fig, ax = plt.subplots()
#                 ax.bar(x.index, x.values, color='crimson')
#                 plt.xticks(rotation=45)
#                 st.pyplot(fig)

#             with col2:
#                 st.dataframe(new_df)

#         st.markdown("---")

#         # --- Word Cloud ---
#         st.markdown("## ☁️ Word Cloud")
#         df_wc = helper.create_wordcloud(selected_user, df)
#         fig, ax = plt.subplots()
#         ax.imshow(df_wc)
#         ax.axis("off")
#         st.pyplot(fig)

#         # --- Common Words ---
#         st.markdown("## 🔠 Most Common Words")
#         most_common_df = helper.most_common_words(selected_user, df)
#         fig, ax = plt.subplots()
#         ax.barh(most_common_df[0], most_common_df[1], color='teal')
#         plt.xticks(rotation=45)
#         st.pyplot(fig)

#         # --- Emoji Analysis ---
#         st.markdown("## 😊 Emoji Analysis")
#         emoji_df = helper.emoji_helper(selected_user, df)
#         if not emoji_df.empty:
#             col1, col2 = st.columns(2)

#             with col1:
#                 st.dataframe(emoji_df)

#             with col2:
#                 fig, ax = plt.subplots()
#                 ax.pie(emoji_df[1].head(), labels=emoji_df[0].head(), autopct="%0.2f", startangle=90)
#                 ax.axis('equal')
#                 st.pyplot(fig)
#         else:
#             print("NOT EMPTY")
        

        
#         # --- Sentiment Analysis ---
#         st.markdown("## ❤️ Sentiment Analysis")

#         # Get sentiment data
#         sentiment_counts = helper.sentiment_analysis(selected_user, df)

#         # Convert to DataFrame
#         import pandas as pd
#         sentiment_df = pd.DataFrame(list(sentiment_counts.items()), columns=["Sentiment", "Message Count"])
#         sentiment_df["Percentage (%)"] = (sentiment_df["Message Count"] / sentiment_df["Message Count"].sum() * 100).round(2)

#         # Create two columns: one for table, one for pie chart
#         col1, col2 = st.columns(2)

#         with col1:
#             st.markdown("### 📋 Sentiment Summary")
#             st.dataframe(sentiment_df.style.format({"Percentage (%)": "{:.2f}"}))

#         with col2:
#             st.markdown("### 📊 Sentiment Distribution")
#             fig, ax = plt.subplots()
#             ax.pie(
#         sentiment_df["Message Count"],
#         labels=sentiment_df["Sentiment"],
#         autopct="%0.2f%%",
#         startangle=90,
#         colors=['#4CAF50', '#9E9E9E', '#F44336']
#     )
#             ax.axis("equal")
#             st.pyplot(fig)

import streamlit as st
import preprocessor, helper
import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd

# --- Page Configuration ---
st.set_page_config(page_title="📊 WhatsApp Chat Analyzer", layout="wide")

# --- Sidebar ---
st.sidebar.title("💬 WhatsApp Chat Analyzer")
uploaded_file = st.sidebar.file_uploader("📂 Upload your chat file")

# --- Main Layout ---
st.markdown("<h1 style='text-align: center; color: #4A4A4A;'>📱 WhatsApp Chat Analyzer</h1>", unsafe_allow_html=True)

if uploaded_file is not None:
    bytes_data = uploaded_file.getvalue()
    data = bytes_data.decode("utf-8")
    df = preprocessor.preprocess(data)

    if df.empty:
        st.warning("🚫 The chat file seems to be empty or could not be processed.")
    else:
        user_list = df['user'].unique().tolist()
        if 'group_notification' in user_list:
            user_list.remove('group_notification')
        user_list.sort()
        user_list.insert(0, "Overall")

        selected_user = st.sidebar.selectbox("👤 Analyze for", user_list)

        if st.sidebar.button("🚀 Show Analysis"):

            # --- Top Statistics ---
            st.markdown("## 🔢 Top Statistics")
            num_messages, words, num_media_messages, num_links = helper.fetch_stats(selected_user, df)
            if num_messages == 0:
                st.info("ℹ️ No messages found for the selected user.")
            else:
                col1, col2, col3, col4 = st.columns(4)
                col1.metric("💬 Messages", num_messages)
                col2.metric("📝 Words", words)
                col3.metric("📸 Media", num_media_messages)
                col4.metric("🔗 Links", num_links)

                st.markdown("---")

                # --- Timelines ---
                st.markdown("## 🗓️ Message Timelines")
                col1, col2 = st.columns(2)

                with col1:
                    timeline = helper.monthly_timeline(selected_user, df)
                    if not timeline.empty:
                        st.markdown("### 📅 Monthly Timeline")
                        fig, ax = plt.subplots()
                        ax.plot(timeline['time'], timeline['message'], color='green')
                        plt.xticks(rotation=45)
                        st.pyplot(fig)
                    else:
                        st.info("📅 No data available for Monthly Timeline.")

                with col2:
                    daily_timeline = helper.daily_timeline(selected_user, df)
                    if not daily_timeline.empty:
                        st.markdown("### 🕘 Daily Timeline")
                        fig, ax = plt.subplots()
                        ax.plot(daily_timeline['only_date'], daily_timeline['message'], color='black')
                        plt.xticks(rotation=45)
                        st.pyplot(fig)
                    else:
                        st.info("🕘 No data available for Daily Timeline.")

                st.markdown("---")

                # --- Activity Maps ---
                st.markdown("## 📊 Activity Maps")
                col1, col2 = st.columns(2)

                with col1:
                    busy_day = helper.week_activity_map(selected_user, df)
                    if not busy_day.empty:
                        st.markdown("### 📆 Most Busy Day")
                        fig, ax = plt.subplots()
                        ax.bar(busy_day.index, busy_day.values, color='purple')
                        plt.xticks(rotation=45)
                        st.pyplot(fig)
                    else:
                        st.info("📆 No activity data for days of the week.")

                with col2:
                    busy_month = helper.month_activity_map(selected_user, df)
                    if not busy_month.empty:
                        st.markdown("### 🗓️ Most Busy Month")
                        fig, ax = plt.subplots()
                        ax.bar(busy_month.index, busy_month.values, color='orange')
                        plt.xticks(rotation=45)
                        st.pyplot(fig)
                    else:
                        st.info("🗓️ No activity data for months.")

                heatmap = helper.activity_heatmap(selected_user, df)
                if heatmap is not None and not heatmap.empty:
                    st.markdown("### 🧭 Weekly Heatmap")
                    fig, ax = plt.subplots()
                    ax = sns.heatmap(heatmap, cmap="YlGnBu")
                    st.pyplot(fig)
                else:
                    st.info("🧭 No heatmap data available.")

                st.markdown("---")

                # --- Busiest Users (Only for Group Analysis) ---
                if selected_user == 'Overall':
                    st.markdown("## 🏆 Most Active Users")
                    x, new_df = helper.most_busy_users(df)
                    if not x.empty:
                        col1, col2 = st.columns(2)
                        with col1:
                            fig, ax = plt.subplots()
                            ax.bar(x.index, x.values, color='crimson')
                            plt.xticks(rotation=45)
                            st.pyplot(fig)
                        with col2:
                            st.dataframe(new_df)
                    else:
                        st.info("🏆 No data for user-wise message activity.")

                st.markdown("---")

                # --- Word Cloud ---
                st.markdown("## ☁️ Word Cloud")
                df_wc = helper.create_wordcloud(selected_user, df)
                if df_wc:
                    fig, ax = plt.subplots()
                    ax.imshow(df_wc)
                    ax.axis("off")
                    st.pyplot(fig)
                else:
                    st.info("☁️ No words available to generate Word Cloud.")

                # --- Common Words ---
                st.markdown("## 🔠 Most Common Words")
                most_common_df = helper.most_common_words(selected_user, df)
                if not most_common_df.empty:
                    fig, ax = plt.subplots()
                    ax.barh(most_common_df[0], most_common_df[1], color='teal')
                    plt.xticks(rotation=45)
                    st.pyplot(fig)
                else:
                    st.info("🔠 No common words found.")

                # --- Emoji Analysis ---
                st.markdown("## 😊 Emoji Analysis")
                emoji_df = helper.emoji_helper(selected_user, df)
                if not emoji_df.empty:
                    col1, col2 = st.columns(2)
                    with col1:
                        st.dataframe(emoji_df)
                    with col2:
                        fig, ax = plt.subplots()
                        ax.pie(emoji_df[1].head(), labels=emoji_df[0].head(), autopct="%0.2f", startangle=90)
                        ax.axis('equal')
                        st.pyplot(fig)
                else:
                    st.info("😊 No emoji data found.")

                # --- Sentiment Analysis ---
                st.markdown("## ❤️ Sentiment Analysis")
                sentiment_counts = helper.sentiment_analysis(selected_user, df)
                if sentiment_counts:
                    sentiment_df = pd.DataFrame(list(sentiment_counts.items()), columns=["Sentiment", "Message Count"])
                    sentiment_df["Percentage (%)"] = (sentiment_df["Message Count"] / sentiment_df["Message Count"].sum() * 100).round(2)

                    col1, col2 = st.columns(2)
                    with col1:
                        st.markdown("### 📋 Sentiment Summary")
                        st.dataframe(sentiment_df.style.format({"Percentage (%)": "{:.2f}"}))

                    with col2:
                        st.markdown("### 📊 Sentiment Distribution")
                        fig, ax = plt.subplots()
                        ax.pie(
                            sentiment_df["Message Count"],
                            labels=sentiment_df["Sentiment"],
                            autopct="%0.2f%%",
                            startangle=90,
                            colors=['#4CAF50', '#9E9E9E', '#F44336']
                        )
                        ax.axis("equal")
                        st.pyplot(fig)
                else:
                    st.info("❤️ No sentiment data found.")

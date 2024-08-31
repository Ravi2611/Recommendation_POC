import streamlit as st
import numpy as np
import pandas as pd
from pages import utils

# @st.cache
def app():
    st.markdown("## Select Recommandation Model You need")

    # Option to select predition type 
    st.info("Please go through below info before selecting the Recoomandation")
    option = st.selectbox(
    "Please Select Your Recommandation Model?",
    ("Collaborative Recommender system", "Content-based recommender system", "Demographic based recommender system","Utility based recommender system","Knowledge based recommender system","Hybrid recommender system"),index=None,
    placeholder="Select recommandation model...")

    st.write("You selected:", option)

    st.info("What are the benefits of Recommendation systems?")
    st.write("""
    1. Improved user experience: Recommendation systems help users discover new products or content that they might be interested in, based on their previous preferences. This can make the user experience more personalized and enjoyable.
    2. Increased sales and engagement: By showing users relevant recommendations, a recommendation system can help drive more traffic to a website or an app, and can encourage users to engage with the content or products being recommended. This can lead to increased sales and revenue for the business.
    3. Enhanced customer loyalty: By providing personalized recommendations, businesses can show customers that they understand their interests and preferences. This helps build customer loyalty and encourage customers to return to the site or app in the future.
    4. Better targeting of marketing campaigns: Recommendation systems can help businesses gather data on customer preferences and interests, which can be used to target marketing campaigns more effectively. This can help businesses reach the right customers with the right messages, which can lead to improved marketing ROI.
    5. Improved efficiency and cost savings: By automating the process of generating recommendations, businesses can save time and resources that would otherwise be spent on manual curation of content or products. This can lead to improved efficiency and cost savings.""")
    st.info("What are the 6 types of recommendation systems?")
    st.write("""
    There are mainly six types of recommendation system.

    1. Collaborative Recommender system
    It’s the most sought after, most widely implemented and most mature technologies that is available in the market. Collaborative recommender systems aggregate ratings or recommendations of objects, recognize commonalities between the users on the basis of their ratings, and generate new recommendations based on inter-user comparisons. The greatest strength of collaborative techniques is that they are completely independent of any machine-readable representation of the objects being recommended and work well for complex objects where variations in taste are responsible for much of the variation in preferences.

    2. Content-based recommender system
    It’s mainly classified as an outgrowth and continuation of information filtering research. In Content-based recommender system, the objects are mainly defined by their associated features. A content-based recommender learns a profile of the new user’s interests based on the features present, in objects the user has rated. It’s basically a keyword specific recommender system here keywords are used to describe the items. Thus, in a content-based recommender system the algorithms used are such that it recommends users similar items that the user has liked in the past or is examining currently.

    3. Demographic based recommender system
    This system aims to categorize the users based on attributes and make recommendations based on demographic classes. Many industries have taken this kind of approach as it’s not that complex and easy to implement. In Demographic-based recommender system the algorithms first need a proper market research in the specified region accompanied with a short survey to gather data for categorization. Demographic techniques form “people-to-people” correlations like collaborative ones, but use different data. The benefit of a demographic approach is that it does not require a history of user ratings like that in collaborative and content based recommender systems.

    4. Utility based recommender system
    Utility based recommender system makes suggestions based on computation of the utility of each object for the user. Of course, the central problem for this type of system is how to create a utility for individual users. In utility based system, every industry will have a different technique for arriving at a user specific utility function and applying it to the objects under consideration. The main advantage of using a utility based recommender system is that it can factor non-product attributes, such as vendor reliability and product availability, into the utility computation. This makes it possible to check real time inventory of the object and display it to the user.

    5. Knowledge based recommender system 
    This type of recommender system attempts to suggest objects based on inferences about a user’s needs and preferences. Knowledge based recommendation works on functional knowledge: they have knowledge about how a particular item meets a particular user need, and can therefore reason about the relationship between a need and a possible recommendation.

    6. Hybrid recommender system
    Combining any of the two systems in a manner that suits a particular industry is known as Hybrid Recommender system. This type of recommendation system is the most sought after Recommender system that many companies look after, as it combines the strengths of more than two Recommender system and also eliminates any weakness which exist when only one recommender system is used.
             
             """)
    st.info("How do you write a recommendation system?")
    st.write("""
    Although machine learning (ML) is commonly used in building recommendation systems, it doesn’t mean it’s the only solution. There are many ways to build a recommendation system? simpler approaches, for example, we may have very few data, or we may want to build a minimal solution fast etc.

    Assume that, for simpler video recommendation,In such that case, based on videos a user has watched, we can simply suggest same authors videos or same publications videos.

    Popularity based
    Easiest way to build a recommendation system is popularity based, simply over all the products that are popular, So how to identify popular products, which could be identified by which are all the products that are bought most.

    For example, In shopping store we can suggest popular dresses by purchase count.

    Classification based
    Second way to build a recommendation system is classification model , In that use feature of both users as well as products in order to predict whether this product liked or not by the user.

    When new users come, our classifier will give a binary value of that product liked by this user or not, In such a way that we can recommend a product to the user.

    Collaborative filtering
    Collaborative filtering models which are based on assumption that people like things similar to other things they like, and things that are liked by other people with similar taste.

    There are two types of collaborative filtering models:

    Nearest neighbor: In these type of recommendation systems are recommending based on nearest neighbors, nearest neighbor approach used to find out either similar users or similar products
    Matrix factorization: It is basically model based collaborative filtering and matrix factorization is the important technique in recommendation system.
             """)
    
    st.info("What are the use Cases and applications of recommendation system")
    st.write("""
    E-Commerce: 
    A recommendation system is very helpful for E-Commerce platforms, it helps provide relevant suggestions to users based on their previous purchases. Recommendation systems help provide personalized offers, product recommendations and recommendations for users with similar tastes. 

    A good recommender system can give a 22.66% lift in conversion rates, on an average.

    Entertainment: 
    Recommendation Models can analyze and understand consumer behavior to detect patterns that can help provide content suggestions to the users. This way a recommendation system is very likely to provide suggestions that will match the user’s needs. 

    This is what Netflix does, by analyzing the user’s tastes and preferences it helps come up with more recommendations for the user.

    Social Media: 
    Social media platforms that have been growing rapidly with millions of active users also use recommendation systems. Social media platforms use recommendation systems to understand the user’s interests, and  analyze their data, to suggest other users with similar interests.

    Travel & hospitality: 
    Recommendation systems are also used to enhance the travel and hospitality platform. It provides the users with personalized travel options and hotel recommendations. Along with that it also helps provide destination suggestions, travel  packages and itineraries 

             """)
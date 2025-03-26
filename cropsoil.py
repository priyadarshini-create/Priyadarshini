import streamlit as st
import base64
import datetime
import pywhatkit as kit

#============================ BACKGROUND IMAGE  ==========================
st.markdown(f'<h1 style="color:#000000;text-align: center;font-size:36px;">{"Soil Recommendation"}</h1>', unsafe_allow_html=True)

def add_bg_from_local(image_file):
    with open(image_file, "rb") as image_file:
        encoded_string = base64.b64encode(image_file.read())
    st.markdown(
    f"""
    <style>
    .stApp {{
        background-image: url(data:image/{"png"};base64,{encoded_string.decode()});
        background-size: cover
    }}
    </style>
    """,
    unsafe_allow_html=True
    )

add_bg_from_local('12.jpg')  # Background image for the app

# Function to recommend suitable soil for the crop
def recommend_soil(crop):
    soil_recommendations = {
        
        'Wheat': 'Loamy soil with good drainage and a pH of 6-7.',
        'Rice': 'Clayey soil with good water retention and a pH of 5.5-7.0.',
        'Tomato': 'Well-drained, slightly acidic to neutral soil with a pH of 6-7.',
        'Corn': 'Loamy or sandy loam soil with good drainage and a pH of 5.8-7.0.',
        'Carrot': 'Sandy loam soil with a pH of 6-7.',
        'Cabbage': 'Loamy, fertile soil with a pH of 6-7.',
        'Potato': 'Loose, well-drained soil with a pH of 5.5-6.5.',
        'Cucumber': 'Well-drained, loamy soil with a pH of 6-7.',
        'Barley': 'Well-drained loamy or sandy loam soil with a pH of 6-7.',
        'Soybean': 'Loamy soil with a pH of 6-7 for optimal nitrogen fixation.',
        'Peanut': 'Sandy loam soil with good drainage and a pH of 5.8-6.5.',
        'Lettuce': 'Fertile, well-drained soil with a pH of 6-7.',
        'Spinach': 'Loamy soil rich in organic matter with a pH of 6-7.5.',
        'Onion': 'Well-drained sandy loam soil with a pH of 6-7.',
        'Garlic': 'Loose, well-drained soil with a pH of 6-7.',
        'Chili': 'Well-drained, slightly acidic soil with a pH of 6-7.',
        'Bell Pepper': 'Loamy, fertile soil with a pH of 6-7.',
        'Strawberry': 'Well-drained sandy loam soil with a pH of 5.5-6.5.',
        'Apple': 'Well-drained, loamy soil with a pH of 6-7.',
        'Banana': 'Rich, well-drained soil with a pH of 5.5-7.0.',
        'Grapes': 'Well-drained, sandy loam soil with a pH of 6-7.',
        'Orange': 'Well-drained, slightly acidic soil with a pH of 6-7.',
        'Mango': 'Well-drained, deep loamy soil with a pH of 5.5-7.5.',
        'Pineapple': 'Well-drained, slightly acidic soil with a pH of 4.5-6.5.',
        'Papaya': 'Well-drained loamy soil with a pH of 5.5-6.5.',
        'Watermelon': 'Sandy loam soil with good drainage and a pH of 6-6.8.',
        'Pumpkin': 'Loamy, fertile soil with a pH of 6-7.',
        'Coconut': 'Well-drained sandy loam or loamy soil with a pH of 5.5-7.',
        'Alfalfa': 'Well-drained loamy soil with a pH of 6.5-7.5.',
        'Cotton': 'Loamy or sandy loam soil with good drainage and a pH of 6-7.',
        'Sugarcane': 'Fertile, well-drained loamy soil with a pH of 6-7.',
        'Sunflower': 'Well-drained, loamy or sandy loam soil with a pH of 6-7.',
        'Peach': 'Well-drained loamy soil with a pH of 6-7.',
        'Pear': 'Loamy soil with good drainage and a pH of 6-7.',
        'Cherry': 'Sandy loam or loamy soil with a pH of 6-7.',
        'Blueberry': 'Well-drained, acidic soil with a pH of 4.5-5.5.',
        'Raspberry': 'Well-drained loamy soil with a pH of 5.5-6.5.',
        'Blackberry': 'Well-drained, slightly acidic soil with a pH of 5.5-6.5.',
        'Avocado': 'Well-drained sandy loam soil with a pH of 5.5-7.0.',
        'Pomegranate': 'Loamy, well-drained soil with a pH of 5.5-7.0.',
        'Fig': 'Loamy or sandy loam soil with a pH of 6-7.',
        'Olive': 'Well-drained, slightly alkaline soil with a pH of 6-8.',
        'Cashew': 'Sandy loam or loamy soil with a pH of 5.5-6.5.',
        'Tea': 'Well-drained, acidic soil with a pH of 4.5-6.0.',
        'Coffee': 'Well-drained, loamy soil with a pH of 5.5-6.5.',
        'Cocoa': 'Well-drained, fertile loamy soil with a pH of 5.5-7.0.',
        'Kiwi': 'Well-drained, sandy loam soil with a pH of 5.5-6.5.',
        'Guava': 'Well-drained, slightly acidic to neutral soil with a pH of 5.5-7.',
        'Lychee': 'Well-drained, fertile soil with a pH of 5.5-7.',
        'Jackfruit': 'Deep, well-drained loamy soil with a pH of 6-7.',
        'Passion Fruit': 'Well-drained, sandy loam soil with a pH of 6-7.',
        'Dragon Fruit': 'Well-drained sandy loam soil with a pH of 5.5-7.',
        'Durian': 'Well-drained, deep loamy soil with a pH of 6-7.',
        'Starfruit': 'Well-drained, slightly acidic soil with a pH of 5.5-6.5.',
        'Gooseberry': 'Well-drained loamy soil with a pH of 5.5-6.5.',
        'Date Palm': 'Well-drained, sandy loam soil with a pH of 6-8.',
        'Taro': 'Loamy, well-drained soil with a pH of 5.5-7.',
        'Yam': 'Sandy loam or loamy soil with good drainage and a pH of 5.5-6.5.',
        'Millet': 'Well-drained loamy or sandy loam soil with a pH of 5.5-7.',
        'Quinoa': 'Well-drained, sandy loam soil with a pH of 6-8.',
        'Sorghum': 'Loamy or sandy loam soil with good drainage and a pH of 5.5-7.',
        'Buckwheat': 'Well-drained, slightly acidic soil with a pH of 5-7.',
        'Sesame': 'Sandy loam or loamy soil with a pH of 5.5-7.',
        'Chickpea': 'Loamy soil with good drainage and a pH of 6-7.'
    
    }

    # Return soil recommendation
    # return soil_recommendations.get(crop, 'No recommendation available for this crop.')



    crop_images = {
        
        'Wheat': 'wheat.jpg',
        'Rice': 'rice.jpg',
        'Tomato': 'tomato.jpg',
        'Corn': 'corn.jpg',
        'Carrot': 'carrot.jpg',
        'Cabbage': 'cabbage.jpg',
        'Potato': 'potato.jpg',
        'Cucumber': 'cucumber.jpg',
        'Barely': 'barely.jfif',
        'Soybean': 'soybean.jfif', 
        'Peanut': 'peanut.jfif', 
        'Lettuce': 'lettuce.jfif', 
        'Spinach': 'spinach.jfif', 
        'Onion': 'onion.jfif', 
        'Gralic': 'gralic.jfif', 
        'Chili': 'chili.jfif', 
        'Bell pepper': 'bell pepper.jfif', 
        'Strawberry': 'strawberry.jfif', 
        'Apple': 'apple.jfif', 
        'Banana': 'banana.jfif', 
        'Grapes': 'grapes.jfif', 
        'Orange': 'orange.jfif', 
        'Mango': 'mango.jfif', 
        'Pineapple': 'pineapple.jfif', 
        'Papaya': 'papaya.jfif', 
        'Watermelon': 'watermelon.jfif', 
        'Pumpkin': 'pumpkin.jfif', 
        'Coconut': 'coconut.jfif', 
        'Alfalfa': 'alfalfa.jfif', 
        'Cotton': 'cotton.jfif', 
        'Sugarcane': 'sugarcane.jfif', 
        'Sunflower': 'sunflower.jfif', 
        'Peach': 'peach.jfif', 
        'Pear': 'pear.jfif', 
        'Cherry': 'cherry.jfif', 
        'Blueberry': 'blueberry.jfif', 
        'Raspberry': 'raspberry.jfif', 
        'Blackberry': 'blackberry.jfif', 
        'Avocado': 'avocado.jfif', 
        'Pomegranate': 'pomegranate.jfif', 
        'Fig': 'fig.jfif', 
        'Olive': 'olive.jfif', 
        'Cashew': 'cashew.jfif', 
        'Tea': 'tea.jfif', 
        'Coffee': 'coffee.jfif', 
        'Cocoa': 'cocoa.jfif', 
        'Kiwi': 'kiwi.jfif', 
        'Guava': 'guava.jfif', 
        'Lychee': 'lychee.jfif', 
        'Jackfruit': 'jackfruit.jfif', 
        'Passion fruit': 'passion fruit.jfif',
        'Durian': 'durian.jfif', 
        'Strawfruit': 'strawfruit.jfif', 
        'Gooseberry': 'gooseberry.jfif', 
        'Date palm': 'date palm.jfif', 
        'Taro': 'taro.jfif', 
        'Yam': 'yam.jfif', 
        'Millet': 'millet.jfif', 
        'Quinoa': 'quinoa.jfif', 
        'Sorghum': 'sorghum.jfif', 
        'Buckwheat': 'buckwheat.jfif', 
        'Sesame': 'sesame.jfif', 
        'Chickpea': 'chickpea.jfif'
        
    }

    soil_images = {
        
        'Wheat': 'loamy_soil.jpg',
        'Rice': 'clay_soil.jpg',
        'Tomato': 'well_drained_soil.jpg',
        'Corn': 'loamy_soil.jpg',
        'Carrot': 'sandy_loam_soil.jpg',
        'Cabbage': 'fertile_soil.jpg',
        'Potato': 'loose_soil.jpg',
        'Cucumber': 'well_drained_soil.jpg',
        'Barley': 'well-drained loamy soil.webp',
        'Soybean': 'well-drained loamy soil.webp',
        'Peanut': 'sandy loam soil.webp',
        'Lettuce': 'fertile, well-drained soil.webp',
        'Spinach': 'sandy loam soil.webp',
        'Onion': 'sandy loam soil.webp',
        'Garlic': 'loose, well-drained soil.webp',
        'Chili': 'sandy loam soil.webp',
        'Bell pepper': 'well-drained loamy soil.webp',
        'Strawberry': 'sandy loam soil.webp',
        'Apple': 'well-drained loamy soil.webp',
        'Banana': 'rich, well-drained loamy soil.webp',
        'Grapes': 'well-drained sandy loam soil.webp',
        'Orange': 'sandy loam soil.webp',
        'Mango': 'well-drained laterite or sandy loam soil.webp',
        'Pineapple': 'sandy loam soil.webp',
        'Papaya': 'well-drained loamy soil.webp',
        'Watermelon': 'sandy loam soil.webp',
        'Pumpkin': 'fertile, well-drained loamy soil.webp',
        'Coconut': 'sandy soil.webp',
        'Alfalfa': 'deep, well-drained loamy soil.webp',
        'Cotton': 'sandy loam soil.webp',
        'Sugarcane': 'well-drained alluvial soil.webp',
        'Sunflower': 'loamy_soil.jpg',
        'Peach': 'sandy loam soil.webp',
        'Pear': 'well-drained loamy soil.webp',
        'Cherry': 'sandy loam soil.webp',
        'Blueberry': 'acidic sandy soil.webp',
        'Raspberry': 'well-drained loamy soil.webp',
        'Blackberry': 'sandy loam soil.wepb',
        'Avocado': 'well-drained sandy loam soil.webp',
        'Pomegranate': 'sandy loam soil.webp',
        'Fig': 'well-drained sandy loam soil.webp',
        'Olive': 'well-drained calcareous soil.webp',
        'Cashew': 'sandy loam soil.webp',
        'Tea': 'acidic, well-drained loamy soil.webp',
        'Coffee': 'well-drained volcanic soil.webp',
        'Cocoa': 'deep, well-drained loamy soil.webp',
        'Kiwi': 'sandy loam soil.webp',
        'Guava': 'well-drained loamy soil.webp',
        'Lychee': 'deep, well-drained loamy soil.webp',
        'Jackfruit': 'sandy loam soil.webp',
        'Passion fruit': 'sandy loam soil.webp',
        'Durian': 'fertile, well-drained loamy soil.webp',
        'Starfruit': 'well-drained loamy soil.webp',
        'Gooseberry': 'well-drained sandy loam soil.webp',
        'Date palm': 'sandy loam soil.webp',
        'Taro': 'moist, well-drained loamy soil.webp',
        'Yam': 'well-drained sandy loam soil.webp',
        'Millet': 'sandy loam soil.webp',
        'Quinoa': 'well-drained sandy loam soil.webp',
        'Sorghum': 'sandy loam soil.webp',
        'Buckwheat': 'well-drained loamy soil.webp',
        'Sesame': 'sandy loam soil.webp',
        'Chickpea': 'sandy loam soil.webp'
   
    }

    descriptions = {
        
        'Wheat': 'Wheat is a staple crop grown in a variety of climates. It thrives in loamy soils with good drainage.',
        'Rice': 'Rice requires soil that can retain water. It grows best in clayey soil, which holds moisture well.',
        'Tomato': 'Tomatoes need slightly acidic soil that drains well to avoid waterlogging, which can affect root health.',
        'Corn': 'Corn grows best in well-drained loamy or sandy loam soil, providing the right nutrients for healthy growth.',
        'Carrot': 'Carrots require loose, sandy loam soil to allow easy root penetration and optimal growth.',
        'Cabbage': 'Cabbage grows well in fertile loamy soils, which offer essential nutrients for robust growth.',
        'Potato': 'Potatoes need loose, well-drained soil to allow for root expansion and prevent rot.',
        'Cucumber': 'Cucumbers thrive in well-drained, loamy soil, which allows the plant to absorb water without root rot.',
        'Barley': 'Barley is a cereal grain commonly used for food, animal feed, and in the production of beverages like beer.',
        'Soybean': 'Soybean is a legume rich in protein and oil, commonly used in food products and as animal feed.',
        'Peanut': 'Peanut is a leguminous plant known for its edible seeds, commonly used in snacks, oils, and butter.',
        'Lettuce': 'Lettuce is a leafy green vegetable often used in salads, sandwiches, and as a garnish.',
        'Spinach': 'Spinach is a nutrient-dense leafy green vegetable, commonly used in salads, smoothies, and cooked dishes.',
        'Onion': 'Onion is a bulbous vegetable with a pungent flavor, used widely in cooking for its aromatic taste.',
        'Garlic': 'Garlic is a flavorful, aromatic bulb used in cooking for its distinctive taste and potential health benefits.',
        'Chili': 'Chilli is a spicy fruit from the Capsicum genus, used to add heat and flavor to dishes.',
        'Bell pepper': 'Bell pepper is a sweet, mild fruit from the Capsicum genus, available in various colors like red, green, and yellow.',
        'Strawberry': 'Strawberry is a sweet, juicy, red fruit with tiny seeds on its surface, known for its vibrant flavor and aroma.',
        'Apple': 'Apple is a crisp, sweet or tart fruit from the Malus genus, available in various colors like red, green, and yellow.',
        'Banana': 'Banana is a soft, sweet, and curved tropical fruit with a yellow peel, rich in potassium and energy.',
        'Grapes': 'Grapes are small, juicy fruits that grow in clusters, available in various colors like green, red, and purple, often eaten fresh or used for juice and wine.',
        'Orange': 'Orange is a juicy, citrus fruit with a sweet-tart flavor and a bright orange peel, rich in vitamin C.',
        'Mango': 'Mango is a sweet, juicy tropical fruit with a vibrant yellow-orange flesh and a distinct aroma.',
        'Pineapple': 'Pineapple is a tropical fruit with spiky skin, juicy golden flesh, and a sweet-tart flavor.',
        'Papaya': 'Papaya is a tropical fruit with orange, juicy flesh, a sweet flavor, and black seeds in the center.',
        'Watermelon': 'Watermelon is a large, refreshing fruit with a green rind, juicy red or pink flesh, and black seeds.',
        'Pumpkin': 'Pumpkin is a large, round, orange fruit with a thick rind, sweet flesh, and edible seeds, often used in cooking and baking.',
        'Coconut': 'Coconut is a tropical fruit with a hard, brown shell, white edible flesh, and refreshing liquid inside.',
        'Alfalfa': 'Alfalfa is a nutrient-rich legume often used as fodder for animals and as a healthy addition to salads and sandwiches.',
        'Cotton': 'Cotton is a soft, fibrous material harvested from the seeds of the cotton plant, widely used in textiles.',
        'Sugarcane': 'Sugarcane is a tall, tropical grass with a sweet, fibrous stalk that is processed to produce sugar and other products.',
        'Sunflower': 'Sunflower is a tall, bright yellow flower with a large, round bloom that turns toward the sun, known for its seeds and oil.',
        'Peach': 'Peach is a juicy, sweet fruit with a fuzzy skin, typically orange or yellow with a red blush, and a pit in the center.',
        'Pear': 'A pear is a sweet, juicy fruit with a smooth skin, typically bell-shaped, and a crisp or soft texture, depending on the variety.',
        'Cherry': 'Cherry is a small, round, sweet or tart fruit, typically red or black, with a pit in the center.',
        'Blueberry': 'Blueberry is a small, round, blue-purple fruit with a sweet-tart flavor, often eaten fresh or used in baking.',
        'Raspberry': 'Raspberry is a small, red or black, sweet-tart berry with a hollow center, often used in desserts and jams.',
        'Blackberry': 'Blackberry is a dark purple to black, sweet-tart berry made up of multiple smaller drupelets, commonly eaten fresh or in jams.',
        'Avocado': 'Avocado is a creamy, green fruit with a large seed in the center, known for its rich texture and healthy fats.',
        'Pomegranate': 'Pomegranate is a round, red fruit filled with juicy, tangy seeds encased in a tough rind, often eaten fresh or used in juice.',
        'Fig': 'Fig is a small, pear-shaped fruit with a sweet, tender flesh and tiny edible seeds, often eaten fresh or dried.',
        'Olive': 'Olive is a small, oval fruit with a bitter taste when raw, often cured and used for oil, salads, and tapenade.',
        'Cashew': 'Cashew is a kidney-shaped nut with a creamy texture and mildly sweet flavor, often eaten as a snack or used in cooking.',
        'Tea': 'Tea is a fragrant, brewed beverage made from the leaves of the Camellia sinensis plant, available in various types like black, green, and herbal.',
        'Coffee': 'Coffee is a popular caffeinated beverage made from roasted coffee beans, known for its bold flavor and energizing effects.',
        'Cocoa': 'Cocoa is a powder made from roasted and ground cacao beans, used in making chocolate and as a flavoring in beverages and desserts.',
        'Kiwi': 'Kiwi is a small, fuzzy fruit with bright green flesh, tiny black seeds, and a sweet-tart flavor.',
        'Guava': 'Guava is a tropical fruit with a sweet, aromatic flavor, green or yellow skin, and pink or white flesh filled with small seeds.',
        'Lychee': 'Lychee is a small, round, tropical fruit with a bumpy red skin, sweet white flesh, and a single large seed.',
        'Jackfruit': 'Jackfruit is a large, green, tropical fruit with a sweet, fibrous yellow flesh and large seeds, often used in savory and sweet dishes.',
        'Passion fruit': 'Passion fruit is a small, round, purple or yellow fruit with a juicy, tangy interior filled with edible seeds.',
        'Dragon fruit': 'Dragon fruit is a vibrant, pink or yellow tropical fruit with a sweet, mildly tangy flesh speckled with small black seeds.',
        'Durian': 'Durian is a large, spiky fruit with a strong odor, creamy, sweet flesh, and a distinctive, custard-like texture.',
        'Starfruit': 'Starfruit is a bright yellow, five-pointed fruit with a tangy-sweet flavor and a star-like shape when sliced.',
        'Gooseberry': 'Gooseberry is a small, round, tart fruit that can be green, yellow, or red, often used in jams and desserts.',
        'Date palm': 'Date palm is a tall tree that produces sweet, chewy dates, commonly eaten as a snack or used in cooking and desserts.',
        'Taro': 'Taro is a starchy root vegetable with a brown, rough skin and purple-tinged flesh, often used in savory dishes or desserts.',
        'Yam': 'Yam is a starchy, sweet root vegetable with a rough skin and orange or white flesh, commonly used in cooking and baking.',
        'Millet': 'Millet is a small, round, nutrient-rich grain often used in baking, porridge, or as a rice alternative.',
        'Quinoa': 'Quinoa is a protein-rich, gluten-free grain with a fluffy texture when cooked, often used in salads and as a side dish.',
        'Sorghum': 'Sorghum is a drought-tolerant, whole grain with a mild flavor, used in cooking, baking, or as animal feed.',
        'Buckwheat': 'Buckwheat is a gluten-free, nutrient-dense grain with a nutty flavor, often used in pancakes, noodles, and porridge.',
        'Sesame': 'Sesame is a small, oil-rich seed with a nutty flavor, often used in cooking, baking, or to make sesame oil and tahini.',
        'Chickpea': 'Chickpea is a round, beige legume with a nutty flavor, commonly used in salads, stews, and to make hummus.'
            
        }

    diseases = {
       
        'Wheat': 'Common wheat diseases include wheat rust, powdery mildew, and wheat yellow rust.',
        'Rice': 'Rice is prone to diseases like rice blast, bacterial blight, and sheath blight.',
        'Tomato': 'Tomatoes can suffer from blight, fusarium wilt, and early blight.',
        'Corn': 'Common corn diseases are corn smut, northern corn leaf blight, and grey leaf spot.',
        'Carrot': 'Carrots can be affected by diseases such as Alternaria leaf blight, Fusarium wilt, and root rot.',
        'Cabbage': 'Cabbage diseases include downy mildew, clubroot, and cabbage root maggot.',
        'Potato': 'Potatoes can face diseases like late blight, early blight, and common scab.',
        'Cucumber': 'Cucumbers are susceptible to downy mildew, powdery mildew, and cucumber mosaic virus.',
        'Barley': 'Good immunity and hygiene keep diseases at bay, Prevention is better than cure.',
        'Soybean': 'Soybeans are affected by diseases like rust, blight, and root rot, Proper crop rotation and fungicides help in management.',
        'Peanut': 'Peanuts suffer from diseases like leaf spot, aflatoxin, and root rot, Timely fungicide application and crop rotation help control them.',
        'Lettuce': 'Lettuce is prone to diseases like downy mildew, bacterial rot, and mosaic virus, Proper spacing, sanitation, and resistant varieties help in management.',
        'Spinach': 'Spinach diseases like downy mildew and leaf spot can be managed with crop rotation and proper drainage.',
        'Onion': 'Onions are affected by diseases like downy mildew and onion rot, managed through crop rotation and fungicides.',
        'Garlic': 'Garlic diseases like white rot and rust can be controlled with crop rotation and proper soil management.',
        'Chili': 'Chilli plants suffer from diseases like bacterial wilt and anthracnose, controlled by proper spacing and fungicide use.',
        'Bell pepper': 'Bell peppers are prone to diseases like bacterial spot and phytophthora blight, managed through crop rotation and fungicides.',
        'Strawberry': 'Strawberry diseases include fungal, bacterial, and viral infections such as gray mold, powdery mildew, and verticillium wilt.',
        'Apple': 'Apple diseases include fungal, bacterial, and viral infections like apple scab, fire blight, and powdery mildew.',
        'Banana': 'Banana diseases include fungal, bacterial, and viral infections such as Panama disease, black Sigatoka, and banana streak virus.',
        'Grapes': 'Grape diseases include fungal, bacterial, and viral infections like downy mildew, powdery mildew, and grapevine leafroll disease.',
        'Orange': 'Orange diseases include fungal, bacterial, and viral infections such as citrus canker, root rot, and tristeza virus.',
        'Mango': 'Mango diseases include fungal, bacterial, and viral infections like anthracnose, powdery mildew, and mango malformation.',
        'Pineapple': 'Pineapple diseases include fungal, bacterial, and viral infections such as heart rot, root rot, and pineapple wilt.',
        'Papaya': 'Papaya diseases include fungal, bacterial, and viral infections like papaya ringspot virus, powdery mildew, and anthracnose.',
        'Watermelon': 'Watermelon diseases include fungal, bacterial, and viral infections such as powdery mildew, bacterial wilt, and watermelon mosaic virus.',
        'Pumpkin': 'Pumpkin diseases include fungal, bacterial, and viral infections like powdery mildew, downy mildew, and cucumber mosaic virus.',
        'Coconut': 'Coconut diseases include fungal, bacterial, and viral infections such as bud rot, coconut leaf wilt, and coconut rhinoceros beetle damage.',
        'Alfalfa': 'Alfalfa diseases include fungal, bacterial, and viral infections like root rot, bacterial wilt, and alfalfa mosaic virus.',
        'Cotton': 'Cotton diseases include bacterial blight, Fusarium wilt, Verticillium wilt, root rot, boll rot, leaf curl virus, and rust, causing yield loss and reduced fiber quality.',
        'Sugarcane': 'Sugarcane diseases include red rot, smut, wilt, rust, ratoon stunting, and mosaic virus, affecting yield and quality.',
        'Sunflower': 'Sunflower diseases include downy mildew, rust, Sclerotinia stem rot, Alternaria leaf spot, and charcoal rot, impacting growth and yield.',
        'Peach': 'Peach diseases include peach leaf curl, brown rot, bacterial spot, powdery mildew, and gummosis, affecting fruit quality and tree health.',
        'Pear': 'Pear diseases include fire blight, powdery mildew, pear scab, bacterial canker, and rust, affecting fruit quality and tree health.',     
        'Cherry': 'Cherry diseases include brown rot, cherry leaf spot, bacterial canker, powdery mildew, and black knot, affecting fruit, leaves, and tree health.',
        'Blueberry': 'Blueberry diseases include mummy berry, botrytis blight, anthracnose, bacterial canker, and root rot, impacting fruit quality and plant health.',
        'Raspberry': 'Raspberry diseases include gray mold, root rot, cane blight, anthracnose, and raspberry mosaic virus, affecting fruit yield and plant vigor.',
        'Blackberry': 'Blackberry diseases include anthracnose, cane blight, orange rust, botrytis fruit rot, and root rot, impacting fruit quality and plant health.',
        'Avocado': 'Avocado diseases include Phytophthora root rot, anthracnose, laurel wilt, sunblotch viroid, and scab, affecting tree health and fruit production.',
        'Pomegranate': 'Pomegranate diseases include wilt, Alternaria fruit rot, bacterial blight, rust, and anthracnose, affecting fruit quality and tree health.',
        'Fig': 'Fig diseases include fig rust, fig mosaic virus, root rot, blight, and anthracnose, impacting fruit production and plant health.',
        'Olive': 'Olive diseases include olive knot, peacock spot, verticillium wilt, olive fruit fly infestation, and tuberculosis, affecting tree health and fruit yield.',
        'Cashew': 'Cashew diseases include powdery mildew, stem and root rot, anthracnose, leaf spot, and fruit and nut borer, impacting tree health and nut production.',
        'Tea': 'Tea diseases include blister blight, leaf spot, root rot, grey blight, and tea rust, affecting plant health and tea yield.',
        'Coffee':'Coffee diseases include coffee rust, coffee berry disease, leaf rust, root rot, and anthracnose, affecting plant health and coffee production.',
        'Cocoa': 'Cocoa diseases include black pod disease, cocoa swollen shoot virus, frosty pod rot, leaf rust, and anthracnose, impacting bean quality and yield.',
        'Kiwi': 'Kiwi diseases include bacterial canker, crown rot, downy mildew, botrytis, and brown spot, affecting fruit quality and plant health.',
        'Guava': 'Guava diseases include anthracnose, bacterial blight, wilt, root rot, and rust, affecting fruit quality and plant health.',
        'Lychee': 'Lychee diseases include powdery mildew, anthracnose, bacterial wilt, root rot, and litchi red pigment disorder, affecting fruit quality and tree health.',
        'Jackfruit': 'Jackfruit diseases include anthracnose, root rot, powdery mildew, fruit rot, and bacterial wilt, impacting fruit quality and tree health.',
        'Passion fruit':'Passion fruit diseases include fusarium wilt, anthracnose, bacterial spot, gray mold, and passion fruit woodiness virus, affecting fruit quality and plant health.',
        'Dragon fruit': 'Dragon fruit diseases include bacterial soft rot, anthracnose, white rot, rust, and powdery mildew, impacting fruit and plant health.',
        'Durian': 'Durian diseases include root rot, durian fruit rot, phytophthora blight, canker, and powdery mildew, affecting fruit quality and tree health.',
        'Starfruit': 'Starfruit diseases include anthracnose, bacterial spot, powdery mildew, root rot, and fruit rot, affecting fruit quality and plant health.',
        'Gooseberry': 'Gooseberry diseases include powdery mildew, anthracnose, rust, downy mildew, and white pine blister rust, affecting fruit and plant health.',
        'Date palm': 'Date palm diseases include bayoud disease, red palm weevil infestation, black scorch, leaf spot, and fusarium wilt, affecting tree health and fruit production.',
        'Taro': 'Taro diseases include leaf blight, root rot, taro rust, bacterial wilt, and taro leaf spot, impacting plant health and tuber yield.',
        'Yam': 'Yam diseases include yam mosaic virus, anthracnose, tuber rot, fusarium wilt, and bacterial soft rot, affecting tuber quality and plant health.',
        'Millet': 'Millet diseases include blast, downy mildew, rust, smut, and ergot, affecting plant health and grain yield.',
        'Quinoa': 'Quinoa diseases include downy mildew, powdery mildew, root rot, fusarium wilt, and cercospora leaf spot, affecting plant health and yield.',
        'Sorghum': 'Sorghum diseases include grain mold, rust, anthracnose, smut, and downy mildew, affecting plant health and grain yield.',
        'Buckwheat': 'Buckwheat diseases include rust, downy mildew, fusarium wilt, anthracnose, and powdery mildew, affecting plant health and seed yield.',
        'Sesame': 'Sesame diseases include leaf spot, powdery mildew, wilt, root rot, and sesame rust, impacting plant health and seed yield.',
        'Chickpea': 'Chickpea diseases include fusarium wilt, ascochyta blight, rust, root rot, and botrytis gray mold, affecting plant health and seed yield.'
    
    }
    

    vitamins = {

        'Wheat': 'Wheat is rich in B-vitamins, especially niacin (B3) and folate (B9).',
        'Rice': 'Rice is a good source of B-vitamins, including B1 (thiamine) and B3 (niacin).',
        'Tomato': 'Tomatoes are high in Vitamin C, Vitamin A, and Vitamin K.',
        'Corn': 'Corn is rich in Vitamin B1 (thiamine), Vitamin C, and folate.',
        'Carrot': 'Carrots are an excellent source of Vitamin A (beta-carotene), Vitamin C, and Vitamin K.',
        'Cabbage': 'Cabbage contains Vitamin C, Vitamin K, and some Vitamin B6.',
        'Potato': 'Potatoes provide Vitamin C, Vitamin B6, and potassium.',
        'Cucumber': 'Cucumbers contain Vitamin K, Vitamin C, and small amounts of B-vitamins.',
        'Barely': 'Barley is rich in B-vitamins, including niacin (B3), thiamine (B1), and pyridoxine (B6).',
        'Soybean': 'Soybeans are a good source of Vitamin K, folate (B9), and Vitamin B2 (riboflavin).',
        'Peanut': 'Peanuts contain Vitamin E, niacin (B3), and folate (B9).',
        'Lettuce': 'Lettuce provides Vitamin A, Vitamin K, and folate (B9).',
        'Spinach': 'Spinach is rich in Vitamin A, Vitamin C, Vitamin K, and folate (B9).',
        'Onion': 'Onions contain Vitamin C, Vitamin B6, and folate (B9).',
        'Gralic': 'Garlic provides Vitamin C, Vitamin B6, and manganese.',
        'Chili': 'Chilies are high in Vitamin C, Vitamin A, and Vitamin B6.',
        'Bell pepper': 'Bell peppers are excellent sources of Vitamin C, Vitamin A, and Vitamin B6.',
        'Strawberry': 'Strawberries are rich in Vitamin C, folate (B9), and manganese.',
        'Apple': 'Apples contain Vitamin C, small amounts of B-vitamins, and potassium.',
        'Banana': 'Bananas provide Vitamin B6, Vitamin C, and potassium.',
        'Grapes': 'Grapes contain Vitamin C, Vitamin K, and B1 (thiamine).',
        'Orange': 'Oranges are high in Vitamin C, Vitamin A, and folate (B9).',
        'Mango': 'Mangoes are rich in Vitamin C, Vitamin A, and Vitamin E.',
        'Pineapple': 'Pineapples provide Vitamin C, Vitamin B1 (thiamine), and manganese.',
        'Papaya': 'Papayas are high in Vitamin C, Vitamin A, and folate (B9).',
        'Watermelon': 'Watermelons contain Vitamin C, Vitamin A, and Vitamin B5 (pantothenic acid).',
        'Pumpkin': 'Pumpkins are rich in Vitamin A (beta-carotene), Vitamin C, and Vitamin E.',
        'Coconut': 'Coconuts provide small amounts of B-vitamins and minerals like manganese and copper.',
        'Alfalfa': 'Alfalfa sprouts are a good source of Vitamin K, Vitamin C, and folate (B9).',
        'Cotton': 'Cotton seeds provide Vitamin E and some B-vitamins.',
        'Sugarcane': 'Sugarcane juice contains Vitamin B1 (thiamine), B2 (riboflavin), and B3 (niacin).',
        'Sunflower': 'Sunflower seeds are rich in Vitamin E, Vitamin B1 (thiamine), and folate (B9).',
        'Peach': 'Peaches provide Vitamin C, Vitamin A, and niacin (B3).',
        'Pear': 'Pears contain Vitamin C, Vitamin K, and small amounts of B-vitamins.',
        'Cherry': 'Cherries are rich in Vitamin C, Vitamin A, and potassium.',
        'Blueberry': 'Blueberries provide Vitamin C, Vitamin K, and manganese.',
        'Raspberry': 'Raspberries are high in Vitamin C, Vitamin K, and folate (B9).',
        'Blackberry': 'Blackberries contain Vitamin C, Vitamin K, and Vitamin A.',
        'Avocado': 'Avocados are rich in Vitamin K, Vitamin E, Vitamin C, and B5 (pantothenic acid).',
        'Pomegranate': 'Pomegranates provide Vitamin C, Vitamin K, and folate (B9).',
        'Fig': 'Figs are a good source of Vitamin B6, Vitamin K, and potassium.',
        'Olive': 'Olives contain Vitamin E, iron, and small amounts of Vitamin A.',
        'Cashew': 'Cashews are rich in Vitamin K, Vitamin E, and B6.',
        'Tea': 'Tea leaves contain Vitamin C, Vitamin B2 (riboflavin), and folate (B9).',
        'Coffee': 'Coffee provides small amounts of B-vitamins, especially niacin (B3).',
        'Cocoa': 'Cocoa is rich in Vitamin B1 (thiamine), B2 (riboflavin), and minerals like magnesium.',
        'Kiwi': 'Kiwis are high in Vitamin C, Vitamin K, and Vitamin E.',
        'Guava': 'Guavas provide Vitamin C, Vitamin A, and folate (B9).',
        'Lychee': 'Lychees are rich in Vitamin C, Vitamin B6, and copper.',
        'Jackfruit': 'Jackfruit contains Vitamin C, Vitamin A, and B-complex vitamins.',
        'Passion fruit': 'Passion fruits are high in Vitamin C, Vitamin A, and fiber.',
        'Durian': 'Durians provide Vitamin C, Vitamin B6, and potassium.',
        'Strawfruit': 'Strawfruits contain Vitamin C, Vitamin A, and potassium.',
        'Gooseberry': 'Gooseberries are rich in Vitamin C, Vitamin A, and manganese.',
        'Date palm': 'Dates are a good source of Vitamin B6, niacin (B3), and riboflavin (B2).',
        'Taro': 'Taro roots provide Vitamin E, Vitamin C, and Vitamin B6.',
        'Yam': 'Yams contain Vitamin C, Vitamin B6, and potassium.',
        'Millet': 'Millets are rich in B-vitamins, especially niacin (B3), thiamine (B1), and folate (B9).',
        'Quinoa': 'Quinoa is a good source of B-vitamins, Vitamin E, and folate (B9).',
        'Sorghum': 'Sorghum provides Vitamin B3 (niacin), Vitamin B6, and Vitamin E.',
        'Buckwheat': 'Buckwheat contains B-vitamins like niacin (B3), riboflavin (B2), and folate (B9).',
        'Sesame': 'Sesame seeds are rich in Vitamin B1 (thiamine), Vitamin B6, and Vitamin E.',
        'Chickpea': 'Chickpeas are a good source of folate (B9), Vitamin B6, and Vitamin C.'
    
    } 
        
    

    yield_info = {
         
         'Wheat': 'The average yield for wheat ranges from 2-4 tons per hectare, depending on soil conditions and climate.',
         'Rice': 'Rice yields can range from 3-8 tons per hectare depending on water availability and soil quality.',
         'Tomato': 'Tomato yield is approximately 20-30 tons per hectare for open field cultivation.',
         'Corn': 'Corn yield can vary from 5 to 10 tons per hectare, depending on soil quality and climate conditions.',
         'Carrot': 'The average yield for carrots is around 25-40 tons per hectare, depending on soil quality and farming practices.',
         'Cabbage': 'Cabbage yield is around 30-40 tons per hectare under ideal conditions.',
         'Potato': 'Potatoes can yield 20-30 tons per hectare, with proper soil conditions and management.',
         'Cucumber': 'Cucumber yield typically ranges from 10 to 20 tons per hectare, depending on the climate and soil.',
         'Barely': 'Barley yields range from 2 to 5 tons per hectare, influenced by soil fertility and rainfall.',
         'Soybean': 'Soybean yields typically range from 2 to 3 tons per hectare, depending on climate and soil quality.',
         'Peanut': 'Peanut yields average 2-4 tons per hectare under optimal conditions.',
         'Lettuce': 'Lettuce yields range from 20 to 30 tons per hectare, depending on variety and growing conditions.',
         'Spinach': 'Spinach yield typically ranges from 10 to 15 tons per hectare with proper irrigation.',
         'Onion': 'Onion yields can range from 25 to 40 tons per hectare with adequate soil management.',
         'Gralic': 'Garlic yield averages 10 to 15 tons per hectare under optimal growing conditions.',
         'Chili': 'Chili yields range from 2 to 5 tons per hectare, depending on variety and farming practices.',
         'Bell pepper': 'Bell pepper yields can range from 20 to 30 tons per hectare under good management.',
         'Strawberry': 'Strawberry yields typically range from 15 to 25 tons per hectare with proper care.',
         'Apple': 'Apple orchards yield about 10 to 30 tons per hectare, depending on variety and climate.',
         'Banana': 'Banana yields range from 30 to 40 tons per hectare under tropical conditions.',
         'Grapes': 'Grape yields typically range from 10 to 15 tons per hectare, depending on vine management.',
         'Orange': 'Orange yields average 20 to 30 tons per hectare under suitable climatic conditions.',
         'Mango': 'Mango orchards yield about 10 to 15 tons per hectare, depending on tree age and climate.',
         'Pineapple': 'Pineapple yields range from 50 to 80 tons per hectare under optimal conditions.',
         'Papaya': 'Papaya yields can reach 40 to 60 tons per hectare with proper management.',
         'Watermelon': 'Watermelon yields average 20 to 40 tons per hectare, depending on soil fertility.',
         'Pumpkin': 'Pumpkin yields range from 20 to 30 tons per hectare under ideal growing conditions.',
         'Coconut': 'Coconut yields range from 10,000 to 12,000 nuts per hectare annually in tropical regions.',
         'Alfalfa': 'Alfalfa yields typically range from 10 to 20 tons per hectare per year when irrigated.',
         'Cotton': 'Cotton yields range from 1 to 3 tons per hectare, influenced by variety and irrigation.',
         'Sugarcane': 'Sugarcane yields can reach 60 to 80 tons per hectare with proper irrigation and fertilization.',
         'Sunflower': 'Sunflower yields range from 1.5 to 3 tons per hectare under optimal conditions.',
         'Peach': 'Peach yields average 10 to 20 tons per hectare, depending on tree density and management.',
         'Pear': 'Pear yields typically range from 15 to 25 tons per hectare under good orchard management.',
         'Cherry': 'Cherry yields range from 8 to 12 tons per hectare, depending on variety and climate.',
         'Blueberry': 'Blueberry yields average 5 to 8 tons per hectare under proper soil conditions.',
         'Raspberry': 'Raspberry yields typically range from 10 to 15 tons per hectare with good management.',
         'Blackberry': 'Blackberry yields range from 10 to 12 tons per hectare under ideal growing conditions.',
         'Avocado': 'Avocado yields range from 7 to 10 tons per hectare, depending on climate and soil.',
         'Pomegranate': 'Pomegranate yields typically range from 10 to 15 tons per hectare with proper care.',
         'Fig': 'Fig yields average 10 to 15 tons per hectare, depending on climate and tree age.',
         'Olive': 'Olive yields range from 2 to 4 tons per hectare in mature orchards.',
         'Cashew': 'Cashew yields range from 1 to 2 tons per hectare under favorable conditions.',
         'Tea': 'Tea yields average 2 to 4 tons per hectare, depending on elevation and climate.',
         'Coffee': 'Coffee yields typically range from 1 to 3 tons per hectare under optimal conditions.',
         'Cocoa': 'Cocoa yields average 1 to 2 tons per hectare in well-managed plantations.',
         'Kiwi': 'Kiwi yields typically range from 20 to 30 tons per hectare under optimal growing conditions.',
         'Guava': 'Guava yields range from 15 to 30 tons per hectare with proper care.',
         'Lychee': 'Lychee yields average 10 to 15 tons per hectare under favorable conditions.',
         'Jackfruit': 'Jackfruit yields typically range from 10 to 20 tons per hectare in tropical climates.',
         'Passion fruit': 'Passion fruit yields range from 15 to 20 tons per hectare under ideal conditions.',
         'Durian': 'Durian yields average 10 to 15 tons per hectare, depending on tree maturity and climate.',
         'Strawfruit': 'Strawfruit yields typically range from 5 to 10 tons per hectare with proper management.',
         'Gooseberry': 'Gooseberry yields range from 10 to 15 tons per hectare under ideal conditions.',
         'Date palm': 'Date palm yields average 10 to 15 tons per hectare in arid regions.',
         'Taro': 'Taro yields range from 10 to 15 tons per hectare, depending on water availability.',
         'Yam': 'Yam yields typically range from 15 to 20 tons per hectare with proper soil management.',
         'Millet': 'Millet yields average 1 to 3 tons per hectare, depending on rainfall and soil fertility.',
         'Quinoa': 'Quinoa yields typically range from 1 to 3 tons per hectare, influenced by altitude and soil quality.',
         'Sorghum': 'Sorghum yields range from 2 to 4 tons per hectare, depending on climate conditions.',
         'Buckwheat': 'Buckwheat yields average 1 to 2 tons per hectare under optimal conditions.',
         'Sesame': 'Sesame yields range from 0.5 to 1.5 tons per hectare, depending on climate and soil type.',
         'Chickpea': 'Chickpea yields typically range from 1 to 2 tons per hectare, depending on soil fertility and rainfall.'
    
    }

    crop_rotation = {

        'Wheat': 'After wheat, plant legumes like peas or beans to fix nitrogen in the soil.',
        'Rice': 'Rotate rice with crops like corn or soybeans to improve soil fertility.',
        'Tomato': 'Tomatoes grow best after crops like lettuce or beans to avoid soil depletion.',
        'Corn': 'Rotate corn with soybeans or wheat for better soil health and pest control.',
        'Carrot': 'After carrots, plant leafy greens like spinach or lettuce.',
        'Cabbage': 'Cabbage grows well after crops like peas or beans, which improve nitrogen content.',
        'Potato': 'Rotate potatoes with legumes or corn to avoid soil degradation.',
        'Cucumber': 'Cucumbers thrive after crops like beans or peas that help with nitrogen fixation.',
        'Barely': 'After barley, rotate with legumes such as clover or beans to replenish soil nitrogen.',
        'Soybean': 'Soybeans add nitrogen to the soil, so follow them with cereal crops like wheat or corn.',
        'Peanut': 'Peanuts enrich soil with nitrogen; rotate them with grains like sorghum or corn.',
        'Lettuce': 'Lettuce can be followed by root crops like carrots or onions for balanced soil use.',
        'Spinach': 'After spinach, plant fruiting crops like tomatoes or peppers for effective rotation.',
        'Onion': 'Onions should be rotated with legumes or leafy vegetables to restore soil nutrients.',
        'Gralic': 'Garlic grows well after legumes and should be followed by leafy greens for soil balance.',
        'Chili': 'Chili grows best after legumes like beans or peas to benefit from nitrogen-rich soil.',
        'Bell pepper': 'Bell peppers grow well after leafy greens or legumes for soil fertility.',
        'Strawberry': 'Strawberries benefit from rotation with legumes or leafy greens to replenish nutrients.',
        'Apple': 'Apple orchards can benefit from cover crops like clover or alfalfa between planting seasons.',
        'Banana': 'Bananas can be rotated with legumes or cover crops to restore soil health.',
        'Grapes': 'Grapes benefit from cover crops like clover or vetch that enhance soil fertility.',
        'Orange': 'Rotate orange orchards with cover crops like legumes to maintain soil productivity.',
        'Mango': 'Mango trees benefit from rotating with nitrogen-fixing cover crops like alfalfa.',
        'Pineapple': 'Pineapples can be followed by legumes like peanuts to improve soil fertility.',
        'Papaya': 'Papaya benefits from rotation with leguminous crops to restore nitrogen in the soil.',
        'Watermelon': 'Watermelons grow well after legumes like beans or peas to improve soil nutrients.',
        'Pumpkin': 'After pumpkins, plant nitrogen-fixing crops like beans or peas for balanced soil.',
        'Coconut': 'Coconut plantations benefit from intercropping with legumes to enhance soil fertility.',
        'Alfalfa': 'Alfalfa enriches soil with nitrogen and should be followed by cereal crops like wheat.',
        'Cotton': 'Rotate cotton with legumes such as peanuts or soybeans to improve soil fertility.',
        'Sugarcane': 'Sugarcane grows well after legumes like soybeans to replenish soil nitrogen levels.',
        'Sunflower': 'Sunflowers should be rotated with legumes or cereals to maintain soil health.',
        'Peach': 'Peach orchards benefit from cover crops like clover or alfalfa to maintain soil fertility.',
        'Pear': 'Pears can be rotated with nitrogen-fixing cover crops like legumes for soil balance.',
        'Cherry': 'Cherries grow well when rotated with cover crops that restore soil nutrients.',
        'Blueberry': 'Blueberries prefer acidic soil; rotate with nitrogen-fixing crops like clover.',
        'Raspberry': 'Raspberries benefit from cover crops like legumes to improve soil quality.',
        'Blackberry': 'Rotate blackberries with legumes to replenish nitrogen and maintain soil structure.',
        'Avocado': 'Avocados thrive when rotated with nitrogen-fixing crops like beans or clover.',
        'Pomegranate': 'Pomegranates benefit from cover crops like alfalfa to maintain soil fertility.',
        'Fig': 'Figs grow well after cover crops like legumes, which restore soil nutrients.',
        'Olive': 'Olive orchards benefit from cover crops like clover or vetch for soil improvement.',
        'Cashew': 'Cashews benefit from nitrogen-fixing cover crops like beans between planting cycles.',
        'Tea': 'Tea plantations benefit from rotating with legumes to restore nitrogen in the soil.',
        'Coffee': 'Coffee plants grow well after cover crops like legumes that improve soil fertility.',
        'Cocoa': 'Cocoa plantations benefit from rotation with legumes or cover crops for nitrogen balance.',
        'Kiwi': 'Kiwis thrive after legumes like clover that improve nitrogen levels in the soil.',
        'Guava': 'Guavas grow best when rotated with legumes or cover crops to enhance soil nutrients.',
        'Lychee': 'Lychee trees benefit from nitrogen-fixing crops like beans for improved soil fertility.',
        'Jackfruit': 'Jackfruit plantations can be rotated with legumes to enhance soil nitrogen levels.',
        'Passion fruit': 'Passion fruit grows well after legumes like beans that restore soil nutrients.',
        'Durian': 'Durian orchards benefit from cover crops like legumes for soil enrichment.',
        'Strawfruit': 'Strawfruit should be rotated with legumes to improve soil nitrogen content.',
        'Gooseberry': 'Gooseberries benefit from nitrogen-fixing crops like beans or peas for soil health.',
        'Date palm': 'Date palms thrive when intercropped with legumes to restore nitrogen in the soil.',
        'Taro': 'Taro grows well after cereal crops and should be rotated with legumes for soil recovery.',
        'Yam': 'Yams benefit from rotation with nitrogen-fixing crops like beans for improved soil quality.',
        'Millet': 'Millet should be rotated with legumes such as cowpeas to restore soil nutrients.',
        'Quinoa': 'Quinoa grows well after legumes that replenish nitrogen in the soil.',
        'Sorghum': 'Sorghum benefits from crop rotation with legumes like soybeans for soil fertility.',
        'Buckwheat': 'Buckwheat should be followed by nitrogen-fixing crops like beans for soil balance.',
        'Sesame': 'Sesame grows well after legumes like peanuts or soybeans to improve soil health.',
        'Chickpea': 'Chickpeas enrich soil with nitrogen; follow them with cereal crops like wheat or corn.'

}


    # Add more recommendations here if desired
    return soil_recommendations.get(crop, 'No recommendation available for this crop.'), crop_images.get(crop, ''), soil_images.get(crop, ''), descriptions.get(crop, ''), diseases.get(crop, ''), vitamins.get(crop, ''), yield_info.get(crop, ''), crop_rotation.get(crop, '')


# Title and instructions
st.write("Select a crop from the dropdown menu to get the most suitable soil recommendation.")

# Dropdown to choose crop
crop = st.selectbox(
    'Select a Crop:',
    ['Wheat', 'Rice', 'Tomato', 'Corn', 'Carrot', 'Cabbage', 'Potato', 'Cucumber', 'Barely', 'Soybean', 'Peanut', 'Lettuce', 'Spinach', 'Onion', 'Gralic', 'chili', 'Bell pepper', 'Strawberry', 
     'Apple', 'Banana', 'Grapes', 'Orange', 'Mango', 'Pineapple', 'Papaya', 'Watermelon', 'Pumpkin', 'Coconut', 'Alfalfa', 'Cotton', 'Sugarcane', 'Sunflower', 'Peach', 'Pear', 'Cherry', 
     'Blueberry', 'Raspberry', 'Blackberry', 'Avocado', 'Pomegranate', 'Fig', 'Olive', 'Cashew', 'Tea', 'Coffee', 'Cocoa', 'Kiwi', 'Guava', 'Lychee', 'Jackfruit', 'Passion fruit', 
     'Durian', 'Strawfruit', 'gooseberry', 'Date palm', 'Taro', 'Yam', 'Millet', 'Quinoa', 'Sorghum', 'Buckwheat', 'Sesame', 'Chickpea']
)

# Button to get the soil recommendation
if st.checkbox('Get Soil Recommendation'):
    recommendation, crop_image, soil_image, description, crop_diseases, crop_vitamins, crop_yield, crop_rotation_info = recommend_soil(crop)
    
    col1, col2, col3 = st.columns(3)
    
    with col1:
        # Display Crop Image and Description
        st.image(crop_image, caption=f"{crop} Image", width=400)
        st.write(f"**Description of {crop}:** {description}")
        
    with col3:
        # Display Soil Recommendation and Soil Image
        st.image(soil_image, caption=f"Recommended soil for {crop}", width=400)
        st.write(f"**Recommended soil for {crop}:** {recommendation}")

    st.write('---------------------------------------------')
    # Display Crop Diseases
    st.write(f"**Common diseases for {crop}:** {crop_diseases}")
    st.write('---------------------------------------------')
    # Display Vitamins
    st.write(f"**Vitamins in {crop}:** {crop_vitamins}")
    st.write('---------------------------------------------')
    # Display Yield Information
    st.write(f"**Expected yield for {crop}:** {crop_yield}")
    st.write('---------------------------------------------')
    # Display Crop Rotation Info
    st.write(f"**Crop rotation suggestion for {crop}:** {crop_rotation_info}")
    st.write('---------------------------------------------')
    with st.sidebar:
        st.map()
    # Add feature for more tips, soil care, and growth stages
    st.write("**Additional Tips:**")
    st.write("Ensure to monitor your soil regularly, use organic amendments, and follow good crop rotation practices to maintain soil fertility.")
    st.write("**Growth Stages Tips:**")
    st.write("1. Germination: Keep the soil moist but not waterlogged.")
    st.write("2. Vegetative Growth: Provide ample sunlight and moderate watering.")
    st.write("3. Flowering/Fruiting: Ensure soil nutrients are balanced for optimal growth.")
    
    # Interactive Crop Map and Crop Care Guide
    st.write("**Soil Care:**")
    st.write("To improve soil fertility, consider composting or using organic fertilizers like manure or green compost.")
    
    # This is a non-interactive version, but could be made interactive in future.
    
    # Button for triggering soil rating
    b2 = st.button('Rating')
    if b2:
        import subprocess
        subprocess.run(['streamlit', 'run', 'ratingpage.py'])
    
#performance tracking by whatsapp
def send_whatsapp_alert(message, phone_number):
    try:
        now = datetime.datetime.now()
        hours = now.hour
        minutes = now.minute + 1  # Send message in the next minute
    
        kit.sendwhatmsg(phone_number, message, hours, minutes)
        print("WhatsApp Alert Sent Successfully!")
    except Exception as e:
        print(f"Error sending alert: {e}")

# Function to detect poor soil performance
def soil_performance_check():
    
        alert_message = "🚨 Soil Performance Alert! Poor soil conditions detected. Immediate action required. 🌱"
        phone_number = "+919363381388"  
        # Replace with recipient's WhatsApp number
        send_whatsapp_alert(alert_message, phone_number)

# Example condition for soil performance tracking

# Button for triggering soil rating
prediction = st.button("predition")

if prediction:  # Assuming 1 represents poor soil condition
    soil_performance_check()
    st.write("Prediction: Soil Performance")
else:
    st.write("Prediction: Good Soil Performance")
    
    
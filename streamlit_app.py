import streamlit as st
from streamlit_elements import Elements

st.set_page_config(
    page_title="Material-UI Button Designer",
    page_icon="🕹️",
)

st.image(
    "https://emojipedia-us.s3.amazonaws.com/source/skype/289/joystick_1f579-fe0f.png",
    width=150,
)
st.title("Material-UI Button Designer")

st.write(
    "Design your Material-UI buttons, add clickable hyperlinks, integrate them in your Streamlit apps! 🎈"
)
st.write("")

with st.form(key="my_form_2"):
    col1, col2 = st.columns(2)
    with col1:
        btn_name = st.text_input("🅰️ Button label", value="Press me!")
        buttonStyle = st.selectbox(
            "🕹️ Button style", ["outlined", "contained", "link"], 1
        )
        color = st.selectbox("🎨 Button color", ["primary", "secondary", "default"], 1)

    with col2:
        hrefLink = st.text_input("🔗 Hyperlink", "https://streamlit.io/")
        size = st.selectbox("📦 Button size", ["small", "medium", "large"], 1)
        icon_selected = st.selectbox(
            "📸 Icon",
            ["no icon", "send", "delete", "save", "chat", "call", "accessible"],
            index=1,
        )

        def get_icon(mt, icon):
            if icon == "no icon":
                pass
            elif icon == "send":
                return mt.icons.send
            elif icon == "delete":
                return mt.icons.delete
            elif icon == "save":
                return mt.icons.save
            elif icon == "chat":
                return mt.icons.chat
            elif icon == "call":
                return mt.icons.call
            elif icon == "accessible":
                return mt.icons.accessible

        st.write("")

    st.form_submit_button("Create your button!")

mt = Elements()
start_icon = get_icon(mt, icon_selected)

st.subheader("Button")

mt.button(
    btn_name,
    target="_blank",
    size=size,
    variant=buttonStyle,
    color=color,
    start_icon=start_icon,
    href=hrefLink,
)
mt.show("zero")

st.subheader("Code")

st.write("First, pip install streamlit-elements")

code = (
    """

import streamlit as st
from streamlit_elements import Elements
mt = Elements()
mt.button("""
    + "'"
    + str(btn_name)
    + "'"
    + """, target="_blank", """
    + """size='"""
    + str(size)
    + "'"
    + """, variant="""
    + "'"
    + str(buttonStyle)
    + "'"
    + """, color="""
    + "'"
    + str(color)
    + "'"
    + """, start_icon="""
    + "'"
    + str(start_icon)
    + "'"
    + """, href="""
    + "'"
    + str(hrefLink)
    + "'"
    + """)

"""
)

code2 = "pip install streamlit-elements"
st.code(code2, language="python")

st.write("Second, add the following code to your Streamlit app")
st.code(code, language="python")

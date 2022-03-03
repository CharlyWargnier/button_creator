import streamlit as st
from streamlit_elements import Elements

st.set_page_config(
    page_title="StreamProphet | Auto-forecasting for Google Search Console",
    page_icon="🔮",
)

st.title("React Button Creator")

st.write("https://v4.mui.com/components/buttons/")

with st.form(key="my_form_2"):
    col1, col2 = st.columns(2)
    with col1:
        btn_name = st.text_input("🅰️ Button label", value="Press me!")
        # st.header("A cat")
        # st.image("https://static.streamlit.io/examples/cat.jpg")
        selectbox = st.selectbox(
            "🕹️ Button style", ["outlined", "contained", "disabled", "link"], 1
        )
        selectbox2 = st.selectbox("🎨 Button color", ["primary", "secondary", "default"], 1)


    with col2:
        # st.header("A dog")
        # st.image("https://static.streamlit.io/examples/dog.jpg")
        size = st.selectbox("📦 Button size", ["small", "medium", "large"], 1)
        # icon = st.selectbox("Icon", ["mt.icons.send", "mt.icons.send", "mt.icons.send"], 1)
        hrefLink = st.text_input("🔗 Hyperlink", "https://www.google.com/")

        icon_selected = st.selectbox("📸 Icon", ["", "send", "delete"])

        def get_icon(mt, icon):
            if icon == "send":
                return mt.icons.send
            elif icon == "delete":
                return mt.icons.delete

        st.write("")

    st.form_submit_button("Create your button!")

# icon = st.selectbox("Icon", ["mt.icons.send", "mt.icons.send", "mt.icons.send"], 1)

# icon_selected = st.selectbox("Icon", ["send", "cancel"])
# mt = Elements()
# icon_map = {
#     "send": mt.icons.send,
#     "cancel": mt.icons.cancel,
# }

# 2
# icons = st.empty()
# mt = Elements()
# icon = icons.selectbox("Icon", [mt.icons.send, mt.icons.send])
# mt.button(..., start_icon=icon, ...)

# 1


mt = Elements()
# mt = Elements()
first_value = get_icon(mt, icon_selected)


# icon_selected = st.selectbox("Icon", ["send", "delete"])

# mt = Elements()
# icon_map = {
#     "send": mt.icons.send,
#     "delete": mt.icons.delete,
# }
#
# if icon_selected == "send":
#     first_value = icon_map["send"]
#
# else:
#     first_value = icon_map["delete"]


col1, col2 = st.columns([1, 2.5])
with col1:

    st.header("Button")

    mt.button(
        f"{btn_name}",
        target="_blank",
        size=size,
        variant=selectbox,
        color=selectbox2,
        start_icon=first_value,
        href=hrefLink,
    )
    mt.show("zero")

with col2:
    st.header("& code!")
    code = (
        """
    
    import streamlit as st
    from streamlit_elements import Elements
    mt = Elements()
    mt.button("""
        + """ variant="""
        + str(selectbox)
        + """, variant2="""
        + str(selectbox2)
        + """, href="""
        + str(hrefLink)
        + """, """
        + """ end text")

    """
    )

    st.code(code, language="python")

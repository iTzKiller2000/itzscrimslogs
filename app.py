import streamlit as st
st.set_page_config(page_title="iTz Scrims - ELO Calculator", page_icon=":trophy:", layout="wide")
st.title ('iTz Scrims - ELO Calculator')
st.subheader ('ELO Calculator made by iTzTomioka_ / _Killer2000_')
st.write ('Insert the ELO of each player to the corresponding box, click the CALCULATE buttom to show the ELO change for each team')
st.write("[Click here if you are not sure how this is supposed to look](https://prnt.sc/z8ZAVsKo95Ss)")
try:
    p1 = int(st.text_input('Player 1 from Winning Team current ELO'))
    p2 = int(st.text_input('Player 2 from Winning Team current ELO'))
    p3 = int(st.text_input('Player 3 from Winning Team current ELO'))
    p4 = int(st.text_input('Player 1 from Losing Team current ELO'))
    p5 = int(st.text_input('Player 2 from Losing Team current ELO'))
    p6 = int(st.text_input('Player 3 from Losing Team current ELO'))
    showcalc = st.button('Calculate')
    if showcalc:
        team1 = int(p1 + p2 + p3) / int(3)
        team2 = int(p5 + p6 + p6) / int(3)
        diff = (team2 - team1)
        difffactor = (team2 + team1) / int(2)
        diffpos = abs(diff)
        diffratio = diff / int(400)
        diffratioex = 10 ** diffratio + 1
        expected = 1 / diffratioex
        if difffactor >= 3200:
            k = 30
        elif difffactor >= 2400:
            k = 50
        elif difffactor < 2399:
            k = 80
        change = k * (1 - expected)
        changew = abs(change)
        changel = -abs(change)
        st.write('The winning team receives {} ELO and the defeated team loses {} ELO '.format(round(changew),
                                                                                               round(changel)))
except:
   st.write('Fill the current box and press ENTER to make the next one appear')
st.text(" ")
st.text(" ")
st.text(" ")
st.text_input('Replay Video (Link to Youtube, Stremable or other platform of choice')
st.text_input('Winning Team members (Discord name/Discord ID)')
st.text_input('Losing Team members (Discord name/Discord ID)')
st.write ("Do not forget to print the page as a PDF and put it in #matchlogs [How?](https://prnt.sc/UtZ8k_WDhiI7)")

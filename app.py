import streamlit as st
import datetime
import numpy as np
from nyct_gtfs import NYCTFeed

st.title('Graham Ave Train Times')

st.secrets["mta_key"]

feed = NYCTFeed("L", api_key=mta_key)
trains = feed.filter_trips(line_id="L", headed_for_stop_id="L12N", underway=True)


def get_times():
    next_trains = []
    for train_num in range(len(trains)):
        stops = trains[train_num].stop_time_updates
        for stop in stops:
            if stop.stop_id == "L12N":
                # Found when the train will arrive
                t_ar = int(abs(stop.arrival - datetime.datetime.now()).seconds / 60)
                if (t_ar > 0) and (t_ar < 40):
                    next_trains.append(t_ar)
                break
    # next_trains.reverse()/
    return next_trains

# if st.button('Refresh Train Times'):
#     feed.refresh()

nt = get_times()

cols = st.columns(len(nt))
for pos, col in enumerate(cols):
    col.subheader(nt[pos])

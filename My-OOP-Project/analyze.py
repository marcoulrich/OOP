from db import counter_data, tracked_habits, show_peroid

def calc_count(db, counter):
    data = counter_data(db, counter)
    return len(data)

def curr_tracked(db, habits):
    data = tracked_habits(db, habits)
    return (data)
    
def same_period(db, habits):
    data = show_peroid(db, habits)
    return (data)
    
def same_streak():
    pass
def longest_streak():
    pass
def longest_for_spec_habit():
    pass
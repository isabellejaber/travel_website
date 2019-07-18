def nyc_activity(activity, walking, crowds):
    if activity == "Shopping":
        if walking == "True" and crowds == "False":
            return "Shopping along Madison Avenue in Manhattan"
        elif walking == "False" and crowds == "True":
            return "Shopping in Bloomingdales or Barneys"
        elif walking == "True" and crowds == "True":
            return "Shopping in Soho"
        else:
            return "Shopping in Soho (make sure to go on a weekday!)"
    elif activity == "Dining":
        if walking == "True" and crowds == "False":
            return "Buy a picnic from Gourmet Garage and head to Central Park"
        elif walking == "False" and crowds == "True":
            return "Grab some hotdogs and eat on the steps of the Met"
        elif walking == "True" and crowds == "True":
            return "Head to Columbus Circle and have a sit down dinner"
        else:
            return 
    elif activity == "Sightseeing":
        if walking == "True" and crowds == "False":
            return "Go to the Brooklyn Promenade and take in Manhattan's skyline"
        elif walking == "False" and crowds == "True":
            return "Head to the top floor of the Empire State building and take in the view"
        elif walking == "True" and crowds == "True":
            return "Go for a walk on the Highline"
        else:
            return "Schedule a bus tour on New York City"
    else:
        return "Did not get that"
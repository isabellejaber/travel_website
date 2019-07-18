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
        return "Sorry there was an error please try again"


def rome_activity(activity, walking, crowds):
    if activity == "Shopping":
        if walking == "True" and crowds == "False":
            return "Walk along Via Urbana and Via del Boschetto"
        elif walking == "False" and crowds == "True":
            return "Go shopping at Centro Commerciale Porta di Roma"
        elif walking == "True" and crowds == "True":
            return "Walk along Via del Corso"
        else:
            return "Go shopping at Centro Commerciale Porta di Roma"
    elif activity == "Dining":
        if walking == "True" and crowds == "False":
            return "Walk through Trastevere and check out all the hip restaurants and bars"
        elif walking == "False" and crowds == "True":
            return "Have lunch at La Moretta and then check out the nearby Tiber River"
        elif walking == "True" and crowds == "True":
            return "Explore the Spanish Steps and then head to Ginger Sapori e Salute for dinner"
        else:
            return 
    elif activity == "Sightseeing":
        if walking == "True" and crowds == "False":
            return "Go for a bike ride or walk along the Via Appia"
        elif walking == "False" and crowds == "True":
            return "Take a guided tour of the Pantheon"
        elif walking == "True" and crowds == "True":
            return "Take a walking tour of the most beautiful fountains in Rome (be sure to see the Trevi Fountain and the Fontana dei Quattro Fiumi!)"
        else:
            return "Rent a golf cart and go for a ride through the Villa Borghese gardens"
    else:
        return "Sorry there was an error please try again"

def brussels_activity(activity, walking, crowds):
    if activity == "Shopping":
        if walking == "True" and crowds == "False":
            return "Walk along Avenue Louise."
        elif walking == "False" and crowds == "True":
            return "Gos shop at Anspach"
        elif walking == "True" and crowds == "True":
            return "Visit the Galerie du Roi"
        else:
            return "Shop online before going to stores."
    elif activity == "Dining":
        if walking == "True" and crowds == "False":
            return "Go have dinner at Rouge Tomate"
        elif walking == "False" and crowds == "True":
            return "Go to Pei and Mei"
        elif walking == "True" and crowds == "True":
            return "Go have some middle eastern food at Al Barmaki"
        else:
            return "Order room service"
    elif activity == "Sightseeing":
        if walking == "True" and crowds == "False":
            return "Go to la Place du Grand Sablon and la Place du Petit Sablon"
        elif walking == "False" and crowds == "True":
            return "Go to la Grand Place to visit the City Hall and the Maison du Roi"
        elif walking == "True" and crowds == "True":
            return "Visit Notre Dame du Sablon"
        else:
            return "Get on a tram and take a ride around Brussels"
    else:
        return "Sorry there was an error please try again"
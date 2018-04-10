from libdistrict.district import District

def efficiency_gap(district_plan, party_a, party_b):
    """
    :param district_plan: an iterable of Districts
    :param party_a: key value / name of party a (Democratic by convention - positive scores denote pro-Democratic asymmetries)
    :param party_b: key value / name of party b (Republican by convention - negative scores denote pro-Republican asymmetries)
    :return: the efficiency gap (positive for party a, negative for party b)
    """

    is_district_plan(district_plan)

    party_a_wasted = 0
    party_b_wasted = 0
    total_votes = 0

    for district in district_plan:
        party_a_votes = district.party_votes[party_a]
        party_b_votes = district.party_votes[party_b]
        total_votes += (party_a_votes + party_b_votes)
        win_threshold = (party_a_votes + party_b_votes) / 2

        if party_a_votes > party_b_votes:
            party_a_wasted += (party_a_votes - win_threshold)
            party_b_wasted += party_b_votes
        elif party_a_votes < party_b_votes:
            party_a_wasted += party_a_votes
            party_b_wasted += (party_b_votes - win_threshold)
        else:
            pass

    return (party_b_wasted - party_a_wasted) / total_votes

def is_district(district):
    if not isinstance(district, District):
        raise TypeError

def is_district_plan(district_plan):
    if district_plan is None:
        raise TypeError
    for district in district_plan:
        is_district(district)
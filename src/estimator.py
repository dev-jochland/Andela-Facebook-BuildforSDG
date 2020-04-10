import math


def calculate_days_factor(days):
    factor = days // 3
    return math.pow(2, factor)


def daysConverter(periodType, userInput):
    if periodType == "days":
        result = calculate_days_factor(userInput)
    elif periodType == "weeks":
        days_conversion = userInput * 7
        result = calculate_days_factor(days_conversion)
    elif periodType == "months":
        days_conversion = userInput * 30
        result = calculate_days_factor(days_conversion)
    return result


def calculate_35_percent_bed(totalNumberOfBeds):
    result = totalNumberOfBeds - totalNumberOfBeds * 0.65
    return math.floor(result)


def estimator(data):
    impact = {}
    severeImpact = {}
    output_dictionary = {"data": data,
                         "impact": impact,
                         "severeImpact": severeImpact}

    impact["currentlyInfected"] = data.get("reportedCases") * 10

    impact["infectionByRequestedTime"] = (math.floor(impact.
                                          get("currentlyInfected") *
                                          calculate_days_factor(
                                              data.get("timeToElapse"))))

    impact["severeCasesByRequestedTime"] = (math.floor(
                                            impact.get
                                            ("infectionByRequestedTime") *
                                            0.15))

    impact["hospitalBedsRequestedTime"] = (calculate_35_percent_bed(
                                           data.get("totalHospitalBeds")) -
                                           impact.get(
                                               "severeCasesByRequestedTime"))

    impact["casesForICUByRequestedTime"] = (math.floor(impact.get
                                            ("infectionByRequestedTime")
                                            * 0.05))

    impact["casesForVentilatorsByRequestedTime"] = (math.floor(
                                                    impact.get(
                                                     "infectionByRequestedTime"
                                                     ) * 0.02))

    impact["dollarsInFlight"] = (impact.get("infectionByRequestedTime")
                                 * 0.71 * 5 * data.get("timeToElapse"))

    severeImpact["currentlyInfected"] = data.get("reportedCases") * 50

    severeImpact["infectionByRequestedTime"] = (math.floor(severeImpact.get(
        "currentlyInfected") * calculate_days_factor(
            data.get("timeToElapse"))))

    severeImpact["severeCasesByRequestedTime"] = (math.floor(
        severeImpact.get("infectionByRequestedTime") * 0.15))

    severeImpact["hospitalBedsRequestedTime"] = (calculate_35_percent_bed(
        data.get("totalHospitalBeds")) - severeImpact.get
        ("severeCasesByRequestedTime"))

    severeImpact["casesForICUByRequestedTime"] = (math.floor(severeImpact.get(
        "infectionByRequestedTime") * 0.05))

    severeImpact["casesForVentilatorsByRequestedTime"] = (math.floor(
        severeImpact.get("infectionByRequestedTime") * 0.02))

    severeImpact["dollarsInFlight"] = (severeImpact.get(
        "infectionByRequestedTime") * 0.71 * 5 * data.get("timeToElapse"))

    return output_dictionary


def main():
    # period_type = input("Select one of the following period type you \
    # wish to estimate\nDays:\nWeeks:\nMonths: ").lower()

    # time_to_elapse = eval(input(f"Input the numbers of {period_type} you \
    # wish to estimate: "))

    # reported_cases = eval(input("Enter the reported cases: "))
    # population = eval(input("Enter the total number of population: "))
    # total_hospital_beds = eval(input("Enter total number of hospital bed: "))

    period_type = "days"
    time_to_elapse = 58
    reported_cases = 674
    population = 66622705
    total_hospital_beds = 1380614

    data = {
        "periodType": period_type,
        "timeToElapse": time_to_elapse,
        "reportedCases": reported_cases,
        "population": population,
        "totalHospitalBeds": total_hospital_beds
    }

    print(estimator(data))


main()

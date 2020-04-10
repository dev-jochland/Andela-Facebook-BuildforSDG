import math


def calculate_days_factor(days):
    factor = days // 3
    return int(math.pow(2, factor))


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
    return int(result)


def estimator(data):
    impact = {}
    severeImpact = {}
    output_dictionary = {"data": data,
                         "impact": impact,
                         "severeImpact": severeImpact}

    impact["currentlyInfected"] = data.get("reportedCases") * 10

    impact["infectionByRequestedTime"] = (impact.
                                          get("currentlyInfected") *
                                          calculate_days_factor(
                                              data.get("timeToElapse")))

    severeImpact["currentlyInfected"] = data.get("reportedCases") * 50

    severeImpact["infectionByRequestedTime"] = (severeImpact.get(
        "currentlyInfected") * calculate_days_factor(
            data.get("timeToElapse")))

    return output_dictionary


def main():
    data = {
            "region": {
             "name": "Africa",
             "avgAge": 19.7,
             "avgDailyIncomeInUSD": 5,
             "avgDailyIncomePopulation": 0.71
            },
            "periodType": "days",
            "timeToElapse": 58,
            "reportedCases": 674,
            "population": 66622705,
            "totalHospitalBeds": 1380614
    }

    print(estimator(data))


main()

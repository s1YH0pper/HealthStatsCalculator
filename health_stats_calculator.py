def calculate_bmi(weight: float, height: float) -> float:
    """
    Calculate the Body Mass Index (BMI) based on weight and height.

    BMI is a commonly used index to assess the weight status and health risks associated with an individual's weight and height.

    Parameters:
    - weight (float): Weight in kilograms.
    - height (float): Height in meters.

    Returns:
    - bmi (float): Body Mass Index value.

    Notes:
    - The weight should be in kilograms and the height should be in meters.
    - The formula used for BMI calculation is weight divided by height squared.
    - The calculated BMI is a numeric value that represents the weight status of an individual.

    Example:
    >>> calculate_bmi(70, 1.75)
    22.86
    """
    bmi = weight / (height**2)
    return bmi


def calculate_bmr(gender: str, weight: float, height: float, age: int) -> float:
    """
    BMR Calculator

    The Basal Metabolic Rate (BMR) is the amount of energy expended by the body at rest to maintain basic physiological functions.

    Formulas used:
    - For males: BMR = (10 * weight) + (6.25 * height) - (5 * age) + 5
    - For females: BMR = (10 * weight) + (6.25 * height) - (5 * age) - 161

    Parameters:
    - gender (str): Gender, can be 'M' for male or 'F' for female.
    - weight (float): Weight in kilograms.
    - height (float): Height in centimeters.
    - age (int): Age in years.

    Returns:
    - bmr (float): Basal Metabolic Rate in calories per day.

    Note:
    - This function uses the Mifflin-St Jeor equation, which is applicable for adults.
    - The calculated result is an estimation and may have some margin of error.

    Example usage:
    >>> calculate_bmr('M', 70, 175, 30)
    1648.75
    >>> calculate_bmr('F', 60, 160, 35)
    1264.0
    """
    if gender == "M":
        bmr = (10 * weight) + (6.25 * height) - (5 * age) + 5
    elif gender == "F":
        bmr = (10 * weight) + (6.25 * height) - (5 * age) - 161
    else:
        raise ValueError(
            "Invalid gender input. Please enter 'M' for male or 'F' for female."
        )
    return bmr


def calculate_max_heart_rate(age: int) -> int:
    """
    Calculate the maximum heart rate based on age.

    The maximum heart rate is an estimate of the highest heart rate a person can achieve during exercise.

    Parameters:
    - age (int): Age in years.

    Returns:
    - max_heart_rate (int): Maximum heart rate.

    Notes:
    - The maximum heart rate is estimated using the formula: 220 - age.
    - This formula provides a rough estimate and individual variations may exist.
    - The calculated maximum heart rate can be used as a reference for exercise intensity.

    Example:
    >>> calculate_max_heart_rate(30)
    190
    """
    max_heart_rate = 220 - age
    return max_heart_rate


def assess_resting_heart_rate(resting_heart_rate: int, age: int) -> str:
    """
    Assess the resting heart rate based on age and compare it with the measured resting heart rate.

    This function compares the measured resting heart rate with the expected range based on age.

    Parameters:
    - resting_heart_rate (int): Measured resting heart rate.
    - age (int): Age in years.

    Returns:
    - assessment (str): Assessment of the resting heart rate.

    Notes:
    - The expected range for resting heart rate can vary depending on age and individual factors.
    - The assessment can provide an indication of whether the measured resting heart rate falls within the expected range.

    Example:
    >>> assess_resting_heart_rate(70, 30)
    'Normal'
    >>> assess_resting_heart_rate(85, 30)
    'High'
    """
    expected_range = get_expected_resting_heart_rate_range(age)

    if resting_heart_rate < expected_range[0]:
        assessment = "Low"
    elif resting_heart_rate > expected_range[1]:
        assessment = "High"
    else:
        assessment = "Normal"

    return assessment


def get_expected_resting_heart_rate_range(age: int) -> tuple:
    """
    Get the expected range for resting heart rate based on age.

    This function provides the expected range for resting heart rate based on age.

    Parameters:
    - age (int): Age in years.

    Returns:
    - expected_range (tuple): Expected range for resting heart rate.

    Notes:
    - The expected range can be defined based on known standards or guidelines.

    Example:
    >>> get_expected_resting_heart_rate_range(30)
    (60, 80)
    """
    if age <= 30:
        expected_range = (60, 80)
    elif age <= 40:
        expected_range = (65, 85)
    elif age <= 50:
        expected_range = (70, 90)
    else:
        expected_range = (75, 95)

    return expected_range


def classify_hypertension(systolic_pressure, diastolic_pressure):
    """
    Classify hypertension based on systolic and diastolic blood pressure values.

    Parameters:
    - systolic_pressure (int): Systolic blood pressure value.
    - diastolic_pressure (int): Diastolic blood pressure value.

    Returns:
    - str: Hypertension classification.

    Notes:
    - The classification is based on the latest blood pressure category guidelines.
    - The classification may vary depending on specific guidelines and practices.

    Example:
    >>> classify_hypertension(130, 85)
    'Stage 1 Hypertension'
    """
    if systolic_pressure < 120 and diastolic_pressure < 80:
        return "Normal Blood Pressure"
    elif systolic_pressure < 130 and diastolic_pressure < 80:
        return "Elevated Blood Pressure"
    elif 130 <= systolic_pressure <= 139 or 80 <= diastolic_pressure <= 89:
        return "Stage 1 Hypertension"
    elif systolic_pressure >= 140 or diastolic_pressure >= 90:
        return "Stage 2 Hypertension"
    elif systolic_pressure >= 180 or diastolic_pressure >= 120:
        return "Hypertensive Crisis"
    else:
        return "Unclassified"


def calculate_max_aspartame_bottle(weight, aspartame_content):
    """
    Calculate the maximum number of bottles a person can consume based on weight and the aspartame content in the drink.

    Parameters:
    - weight (float): Weight of the person in kilograms.
    - aspartame_content (float): Aspartame content in milligrams in a single bottle of the drink.

    Returns:
    - int: Maximum number of bottles that can be consumed in a day.

    Notes:
    - The calculation assumes that the maximum daily intake of aspartame is 40mg/kg of body weight.
    - The aspartame content should be provided in milligrams (mg).
    - The weight should be provided in kilograms (kg).
    - The result is rounded down to the nearest whole number.

    Example:
    >>> calculate_max_aspartame_bottle(70, 250)
    18
    """
    max_aspartame_intake = 40 * weight
    max_bottles = max_aspartame_intake // aspartame_content
    return max_bottles


if __name__ == "__main__":
    pass

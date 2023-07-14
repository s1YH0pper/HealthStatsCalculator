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

if __name__=="__main__":
    pass
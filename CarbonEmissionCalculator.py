class CarbonEmissionCalculator:
    @staticmethod
    def calculate_carbon_emission(email_count):
        carbon_emission_per_email = 0.02
        total_emission = email_count * carbon_emission_per_email
        return total_emission

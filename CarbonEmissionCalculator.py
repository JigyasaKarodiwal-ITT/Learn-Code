class CarbonEmissionCalculator:
    @staticmethod
    def calculateCarbonEmission(emailCount):
        carbonEmissionPerEmail = 0.02
        totalEmission = emailCount * carbonEmissionPerEmail
        return totalEmission

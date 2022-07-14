from model import RecommendationSystem

if __name__ == '__main__':
    system = RecommendationSystem()
    system.preprocessing()
    system.implementation()
    system.retrieve_top_associations()

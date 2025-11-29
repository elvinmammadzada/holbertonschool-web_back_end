#!/usr/bin/env python3
"""
10-update_topics.py
Change all topics of a school document based on the name
"""

def update_topics(mongo_collection, name, topics):
    """
    mongo_collection: pymongo collection object
    name: string, school name to update
    topics: list of strings, new topics
    """
    mongo_collection.update_one(
        {"name": name},
        {"$set": {"topics": topics}}
    )

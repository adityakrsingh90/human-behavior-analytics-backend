"""
This file documents database schema used in Supabase
"""

# user_predictions
"""
id (uuid)
user_id (uuid)
productivity_score (float)
burnout_score (float)
archetype (text)
created_at (timestamp)
"""

# user_feedback
"""
id (uuid)
user_id (uuid)
prediction_id (uuid)
is_accurate (boolean)
created_at (timestamp)
"""

def export_summary(rows):
    return {"count": len(rows), "ids": [row[0] for row in rows]}

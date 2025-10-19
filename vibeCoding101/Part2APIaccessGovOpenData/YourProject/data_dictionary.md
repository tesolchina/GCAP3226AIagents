# Data Dictionary Template

Document your data structure here. AI can help you generate this based on your dataset.

---

## Dataset Information

**Dataset Name**: [Your dataset name]

**Source**: [DATA.GOV.HK or other source]

**Last Updated**: [Date]

**Update Frequency**: [Real-time / Daily / Weekly / etc.]

---

## Data Fields

### Field 1: [field_name]
- **Type**: [String / Integer / Float / Date / Boolean]
- **Description**: [What this field represents]
- **Example**: [Sample value]
- **Required**: [Yes / No]
- **Possible Values**: [If limited, list them]

### Field 2: [field_name]
- **Type**: [String / Integer / Float / Date / Boolean]
- **Description**: [What this field represents]
- **Example**: [Sample value]
- **Required**: [Yes / No]
- **Possible Values**: [If limited, list them]

### Field 3: [field_name]
- **Type**: [String / Integer / Float / Date / Boolean]
- **Description**: [What this field represents]
- **Example**: [Sample value]
- **Required**: [Yes / No]
- **Possible Values**: [If limited, list them]

---

## Data Structure

### JSON Format Example
```json
{
  "field1": "example value",
  "field2": 123,
  "field3": 45.67,
  "nested_object": {
    "subfield1": "value",
    "subfield2": "value"
  }
}
```

### CSV Format Example
```csv
field1,field2,field3
value1,123,45.67
value2,456,78.90
```

---

## Data Quality Notes

### Known Issues
- [List any known data quality issues]
- [Missing values for certain fields]
- [Data gaps or anomalies]

### Data Cleaning Required
- [ ] Remove duplicates
- [ ] Handle missing values
- [ ] Standardize formats
- [ ] Filter invalid records
- [ ] Other: ___________

---

## Units and Measurements

| Field | Unit | Precision |
|-------|------|-----------|
| [field_name] | [meters/kg/etc.] | [2 decimal places] |
| [field_name] | [meters/kg/etc.] | [2 decimal places] |

---

## Codes and Categories

### Category Codes
| Code | Description | Notes |
|------|-------------|-------|
| [CODE1] | [Description] | [Additional info] |
| [CODE2] | [Description] | [Additional info] |

---

## Sample Data

```
[Paste 3-5 sample records here to illustrate the data structure]
```

---

## Data Access Notes

### API Parameters
- **Required**: [List required parameters]
- **Optional**: [List optional parameters]

### Rate Limits
- [Any known rate limits or restrictions]

### Authentication
- [None / API Key / OAuth / etc.]

---

*AI can help you fill this out after analyzing your dataset!*

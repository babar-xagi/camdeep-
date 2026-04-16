# 🏫 School Management Guide - CAMDEEP

## How Schools Appear on Frontend

Schools will **ONLY** appear on the public website school listing page when **BOTH** of these conditions are met:

✅ **Condition 1**: Status = "Active"  
✅ **Condition 2**: MOU Signed = Checked (✓)

---

## 📋 Step-by-Step: Adding a New School

### Step 1: Go to Admin Panel
```
Navigate to: http://localhost:8000/admin/
Login with your superuser credentials
```

### Step 2: Access Schools Section
```
Click on "Schools" in the admin sidebar
Click "Add School" button (top right)
```

### Step 3: Fill in School Information

**Required Fields:**

1. **Name** (Required)
   - Example: "Superior College Lahore"
   
2. **Slug** (Auto-generated, but you can customize)
   - Example: "superior-college-lahore"
   - This is used in the URL

3. **Description** (Required)
   - Write a brief description of the school
   - Example: "A premier educational institution..."

4. **Principal Information**
   - Principal Name (Required)
   - Principal Email (Required)
   - Principal Phone (Required)

5. **Administrator Contact**
   - CAMDEEP Coordinator Name (Optional)
   - Admin Email (Optional)
   - Admin Phone (Optional)

6. **Address** (All Required)
   - Street Address
   - City
   - State/Province
   - Postal Code
   - Country

7. **School Details**
   - Total Students (Number of students enrolled)
   - Target Grades (e.g., "6,7,8,9,10" or "9,10")
   - Website (Optional)
   - Established Year (Optional)
   - Logo (Optional image upload)

### Step 4: Set Partnership Status (IMPORTANT!)

**In the "Partnership & Frontend Display" section:**

1. **Status** - Select "Active" 
   - Options: Pending, Active, Inactive, Archived
   - Only "Active" schools appear on frontend

2. **MOU Signed** - CHECK THIS BOX ✓
   - Must be checked for the school to appear on frontend
   - MOU Date: Select the date when MOU was signed

### Step 5: Review Frontend Requirements
- You'll see a green box showing:
  - ✓ Status: Active
  - ✓ MOU Signed: Yes
  - **✓ School WILL appear on frontend school listing**

### Step 6: Save the School
- Click "Save and continue editing" or "Save" button
- The school is now created!

---

## 🔍 Making Schools Visible on Frontend

### Important Requirements:

After creating a school, ensure:

```
Status: ✓ Active (NOT "Pending", "Inactive", or "Archived")
MOU Signed: ✓ Checked (Must have checkmark)
```

### What Happens When You Save:

✅ **If Status = Active AND MOU Signed = YES**
- School appears on: http://localhost:8000/schools/
- School details page is accessible
- School is listed in grid view with other active schools
- MOU Signed badge appears on school card

❌ **If Status ≠ Active OR MOU Signed = NO**
- School does NOT appear on frontend
- You'll see message: "No partner schools yet"
- Admin can still see and manage the school in admin panel

---

## 📊 Admin List View Features

In the Schools list (http://localhost:8000/admin/schools/school/):

**Columns Shown:**
- **Name**: School name
- **City**: Location
- **Status**: Current status (Pending/Active/Inactive/Archived)
- **MOU Signed**: Whether MOU is signed (Yes/No)
- **Appears on Frontend?**: 
  - ✓ Yes (green) - School will be visible on frontend
  - ✗ No (red) - School will NOT be visible on frontend

**Filters Available:**
- Filter by Status (Active, Inactive, etc.)
- Filter by MOU Signed (Yes/No)
- Filter by City or State
- Search by Name or Email

---

## 📝 Example: Adding "Superior College"

### Admin Form Entry:

```
Name: Superior College Lahore
Slug: superior-college-lahore
Description: A premier educational institution providing quality education 
             for students from Grade 6-10.

Principal Name: Dr. Muhammad Ahmed
Principal Email: principal@superior-college.edu
Principal Phone: +92 300 1234567

Admin Contact Name: Fatima Khan
Admin Email: fatima@superior-college.edu
Admin Phone: +92 300 9876543

Street Address: Main Ferozepur Road
City: Lahore
State: Punjab
Postal Code: 54000
Country: Pakistan

Total Students: 450
Target Grades: 6,7,8,9,10
Website: https://superior-college.edu
Established Year: 1985
Logo: (upload school logo image)

Status: Active  ✓ (IMPORTANT!)
MOU Signed: ✓ (IMPORTANT!)
MOU Date: 2026-04-16
```

### Result:
✓ School appears on frontend at http://localhost:8000/schools/
✓ Shows with green "MOU Signed" badge
✓ Clickable to view full school details

---

## 🔐 Admin Actions

### Editing an Existing School:
1. Go to Schools list in admin
2. Click on school name to edit
3. Change Status or MOU Signed as needed
4. Click Save
5. Changes appear immediately on frontend (if conditions met)

### Deactivating a School:
- Change Status from "Active" to "Inactive"
- School immediately disappears from frontend
- Data is preserved in database

### Reactivating a School:
- Change Status back to "Active"
- Ensure MOU Signed is still checked
- School reappears on frontend

---

## ⚠️ Common Issues & Solutions

### Issue 1: School doesn't appear on frontend after adding
**Solution**: Check that:
- [ ] Status = "Active" (not "Pending" or "Inactive")
- [ ] MOU Signed checkbox is checked ✓
- [ ] Refresh browser page (Ctrl+F5)

### Issue 2: School status shows "✗ No" in admin list
**Possible Reasons**:
- Status is not "Active"
- MOU Signed checkbox is not checked
- **Fix**: Click on school, update both fields, and save

### Issue 3: Frontend still shows "No partner schools yet"
**Check**:
- Did you save the school?
- Is status "Active"?
- Is MOU Signed checked?
- Try refreshing the page
- Check if there are any other schools (they should all be visible if conditions met)

---

## 📱 Frontend Display

### How Schools Appear on Frontend:

```
School Card Shows:
┌─────────────────────────────────┐
│ Superior College Lahore    ✓    │
│ Lahore, Punjab         MOU Signed│
│                                 │
│ A premier educational insti...  │
│                                 │
│ Principal: Dr. Muhammad Ahmed   │
│ Students: 450                   │
│ Established: 1985               │
│                                 │
│ [View Details]  [Visit Website] │
└─────────────────────────────────┘
```

**Clicking "View Details" leads to school's detail page**

---

## 📊 Database Schema Note

**Schools Table Fields:**

| Field | Type | Required | Notes |
|-------|------|----------|-------|
| name | String | Yes | School name |
| slug | String | Yes | URL slug |
| status | Choice | Yes | pending/active/inactive/archived |
| mou_signed | Boolean | No | MOU signature checkbox |
| mou_date | Date | No | Date MOU was signed |
| principal_name | String | Yes | Principal full name |
| principal_email | Email | Yes | Principal contact email |
| principal_phone | String | Yes | Principal phone number |

**Frontend Visibility Logic:**
```python
if school.status == 'active' AND school.mou_signed == True:
    # School appears on frontend
    schools_list.append(school)
else:
    # School does NOT appear on frontend
    pass
```

---

## 🎯 Best Practices

1. **Always check both conditions** before saving
2. **Set MOU Date** when you check the MOU Signed box
3. **Use descriptive descriptions** for better frontend display
4. **Upload school logo** for professional appearance
5. **Keep contact information updated** for communication
6. **Change status to Inactive** rather than deleting (preserves data)

---

## 🚀 Quick Checklist for Adding Schools

```
☐ Go to http://localhost:8000/admin/schools/school/
☐ Click "Add School" button
☐ Fill all required fields (Name, Email, Phone, Address)
☐ Enter Principal information
☐ Set Status to "Active" ⭐ IMPORTANT
☐ Check "MOU Signed" ⭐ IMPORTANT
☐ Set MOU Date
☐ Click Save
☐ Visit http://localhost:8000/schools/ to verify
☐ School should now be visible! ✓
```

---

## 📞 Support

If schools are not appearing:
1. Verify Status is "Active"
2. Verify MOU Signed is checked ✓
3. Refresh the browser page
4. Check admin list to see "Appears on Frontend?" column

**Need Help?**
- Review the "Partnership & Frontend Display" section in school form
- Check the green status box showing frontend requirements
- Look at admin list column "Appears on Frontend?"

---

**Last Updated**: April 16, 2026  
**Version**: 1.0.0  
**Platform**: CAMDEEP Django 6.0.4


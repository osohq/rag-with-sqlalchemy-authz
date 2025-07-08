actor User {}

resource Department { # HR, Engineering
  roles = ["manager", "member"];
}

resource Document {
  # roles are groups of permissions
  roles = ["reader", "editor"];
  
  # permissions are the actions that can be performed on the resource
  permissions = ["read", "edit", "delete"];
  
  # relationships
  relations = { 
    department: Department,
    creator: User
  };

  # RBAC
  "read" if "reader";
  "edit" if "editor";
  "reader" if "editor";

  # ReBAC
  "editor" if "creator";
  "delete" if "creator";
  "reader" if "manager" on "department";

  # ABAC
  "read" if is_public(resource);
}

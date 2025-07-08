actor User {}

resource Department { # HR, Engineering
  # roles are groups of permissions
  roles = ["admin", "manager", "member"];
  # permissions are the actions that can be performed on the resource
  permissions = ["add_member", "read"];
  
  # permissions assignment
  "read" if "member";
  "add_member" if "admin";

  # role inheritence
  "member" if "manager";
  "manager" if "admin";
}

resource Document {
  roles = ["reader", "editor"];
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
  "reader" if "member" on "department";

  # ABAC
  "read" if is_public(resource);
}

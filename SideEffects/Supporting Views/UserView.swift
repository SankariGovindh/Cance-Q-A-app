//
//  UserView.swift
//  SideEffects
//
//  Created by Kevin Tran on 11/15/19.
//  Copyright © 2019 Kevin Tran. All rights reserved.
//

import SwiftUI

struct UserView: View {
    @State private var showingAlert = false
    @State private var selection: Int? = nil

    @Environment(\.presentationMode) var mode: Binding<PresentationMode>
    
    @EnvironmentObject var userData: UserData
    @State private var networkManager = NetworkManager()
    
    var body: some View {
        ScrollView {
            VStack {
                Text("New User").font(Font.system(size: 60, design: .default))
                HStack {
                    Text("First Name")
                TextField("First Name", text: $userData.firstname, onEditingChanged: { isEditing in }).foregroundColor(.primary).padding().textFieldStyle(RoundedBorderTextFieldStyle())

                    Button(action: {
                     self.userData.firstname = ""
                    }) {
                    Image(systemName: "xmark.circle.fill").opacity(userData.firstname == "" ? 0 : 1)
                    }
                }.padding().offset(y:10)
                
                HStack {
                    Text("Last Name")
                 TextField("Last Name", text: $userData.lastname, onEditingChanged: { isEditing in
                        }).foregroundColor(.primary).padding().textFieldStyle(RoundedBorderTextFieldStyle())

                    Button(action: {
                     self.userData.lastname = ""
                    }) {
                     Image(systemName: "xmark.circle.fill").opacity(userData.lastname == "" ? 0 : 1)
                    }
                }.padding().offset(y:-10)
             
                 HStack {
                 Text("Username")
                     TextField("Username", text: $userData.username, onEditingChanged: { isEditing in
                         }).foregroundColor(.primary).padding()  .textFieldStyle(RoundedBorderTextFieldStyle())

                     Button(action: {
                         self.userData.username = ""
                     }) {
                         Image(systemName: "xmark.circle.fill").opacity(userData.username == "" ? 0 : 1)
                     }
                 }.padding().offset(y:-20)
             
                 HStack {
                 Text("Password")
                     TextField("Password", text: $userData.password, onEditingChanged: { isEditing in
                         }).foregroundColor(.primary).padding()  .textFieldStyle(RoundedBorderTextFieldStyle())

                     Button(action: {
                         self.userData.password = ""
                     }) {
                         Image(systemName: "xmark.circle.fill").opacity(userData.password == "" ? 0 : 1)
                     }
                 }.padding().offset(y:-30)
             
                 HStack {
                 Text("Email")
                     TextField("Email", text: $userData.email, onEditingChanged: { isEditing in
                         }).foregroundColor(.primary).padding()  .textFieldStyle(RoundedBorderTextFieldStyle())

                     Button(action: {
                         self.userData.email = ""
                     }) {
                         Image(systemName: "xmark.circle.fill").opacity(userData.email == "" ? 0 : 1)
                     }
                 }.padding().offset(y:-40)
             
                 Button(action: {
                    
                    self.networkManager.post(code: 2, uploadData: self.userData.create_keys_values(), completionHandler: { flag, _  in
                        if flag == true {
                            self.showingAlert = true
                            self.mode.wrappedValue.dismiss()
                        }
                    })
                 })
                 {
                     Text("Submit")
                         .padding()
                         .foregroundColor(.white)
                         .background(LinearGradient(gradient: Gradient(colors: [Color.red,  Color.purple]), startPoint: .leading, endPoint: .trailing))
                         .cornerRadius(40)
                 }.alert(isPresented: $showingAlert) {
                     Alert(title: Text("Account"), message: Text("Created Successfully"), dismissButton: .default(Text("Okay")))
                 }
            }
        }
    }
}

struct UserView_Previews: PreviewProvider {
    static var previews: some View {
        UserView()
    }
}
